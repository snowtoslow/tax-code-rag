"""Retrieve relevant chunks and answer using the configured generation provider."""

import os
import sys

import chromadb
from dotenv import load_dotenv

from docling_pdf.clients import AnswerClient, create_client
from docling_pdf.embeddings import COLLECTION_NAME, embedding_function

load_dotenv()

SYSTEM_PROMPT = (
    "Answer using only the provided context. Cite sources like [1], [2]. "
    "If the context doesn't contain the answer, say so. "
    "Answer in the language of the question."
)


def generate_answer(contents: str, *, client: AnswerClient | None = None) -> str:
    generator = client if client is not None else create_client()
    return generator.generate(contents=contents, system_prompt=SYSTEM_PROMPT)


def answer(question: str, k: int = 12, *, client: AnswerClient | None = None) -> str:
    collection = chromadb.PersistentClient(path=os.environ["CHROMA_PATH"]).get_collection(
        COLLECTION_NAME, embedding_function=embedding_function()
    )
    hits = collection.query(query_texts=[question], n_results=k)

    context = "\n\n".join(
        f"[{n}] ({meta['source']}, {meta['headings']})\n{doc}"
        for n, (doc, meta) in enumerate(
            zip(hits["documents"][0], hits["metadatas"][0]), start=1
        )
    )

    return generate_answer(
        f"Context:\n{context}\n\nQuestion: {question}", client=client,
    )


if __name__ == "__main__":
    print(answer(" ".join(sys.argv[1:])))
