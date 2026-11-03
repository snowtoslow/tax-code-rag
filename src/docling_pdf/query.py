"""Retrieve relevant chunks and answer a question with Gemini."""

import os
import sys
import time

import chromadb
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

load_dotenv()

MODEL = os.environ["GEMINI_MODEL"]
FALLBACK_MODEL = os.environ["GEMINI_FALLBACK_MODEL"]

SYSTEM_PROMPT = (
    "Answer using only the provided context. Cite sources like [1], [2]. "
    "If the context doesn't contain the answer, say so. "
    "Answer in the language of the question."
)


def generate_with_retry(client, contents: str, retries: int = 4) -> str:
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.2,
    )
    for model in (MODEL, FALLBACK_MODEL):
        for attempt in range(retries):
            try:
                response = client.models.generate_content(
                    model=model, contents=contents, config=config
                )
                return response.text
            except errors.ServerError as e:  # 5xx: overloaded / unavailable
                wait = 2**attempt  # 1s, 2s, 4s, 8s
                print(f"[{model}] {e.code} (attempt {attempt + 1}/{retries}), "
                      f"retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
        print(f"[{model}] still unavailable, trying fallback...", file=sys.stderr)
    raise RuntimeError("Gemini is unavailable on all configured models. Try again later.")


def answer(question: str, k: int = 5) -> str:
    collection = chromadb.PersistentClient(path="chroma_db").get_collection("docs")
    hits = collection.query(query_texts=[question], n_results=k)

    context = "\n\n".join(
        f"[{n}] (page {meta['page']}, {meta['headings']})\n{doc}"
        for n, (doc, meta) in enumerate(
            zip(hits["documents"][0], hits["metadatas"][0]), start=1
        )
    )

    client = genai.Client()  # reads GEMINI_API_KEY
    return generate_with_retry(
        client, f"Context:\n{context}\n\nQuestion: {question}"
    )


if __name__ == "__main__":
    print(answer(" ".join(sys.argv[1:])))