"""Parse HTML with Docling, chunk it, and index the chunks in Chroma."""

import sys
from io import BytesIO
from pathlib import Path

import chromadb
from bs4 import BeautifulSoup
from docling.chunking import HybridChunker
from docling.datamodel.base_models import DocumentStream
from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer

from dotenv import load_dotenv

from docling_pdf.embeddings import COLLECTION_NAME, EMBEDDING_MODEL, embedding_function

import os

load_dotenv()
CHROMA_PATH = os.environ["CHROMA_PATH"]

# mPDF-specific, non-standard tags that would leak into the text
MPDF_TAGS = [
    "htmlpageheader", "htmlpagefooter", "sethtmlpageheader", "sethtmlpagefooter",
    "setpageheader", "setpagefooter", "pagebreak", "tocentry", "bookmark",
    "indexentry", "annotation", "script", "style", "nav",
]


def clean_html(path: Path) -> str:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for tag in soup.find_all(MPDF_TAGS):
        tag.decompose()
    return str(soup)


def ingest(paths: list[Path], collection_name: str = COLLECTION_NAME) -> None:
    converter = DocumentConverter()
    # chunker = HybridChunker()
    tokenizer = HuggingFaceTokenizer.from_pretrained(
        model_name=EMBEDDING_MODEL,
        max_tokens=1024,
    )
    chunker = HybridChunker(tokenizer=tokenizer)
    collection = chromadb.PersistentClient(path=CHROMA_PATH).get_or_create_collection(
        collection_name,
        embedding_function=embedding_function(),
        metadata={"hnsw:space": "cosine"},
    )

    for path in paths:
        stream = DocumentStream(
            name=path.name, stream=BytesIO(clean_html(path).encode("utf-8"))
        )
        doc = converter.convert(stream).document
        chunks = list(chunker.chunk(dl_doc=doc))

        ids, texts, metadatas = [], [], []
        for i, chunk in enumerate(chunks):
            ids.append(f"{path.stem}-{i}")
            texts.append(chunker.contextualize(chunk=chunk))
            metadatas.append(
                {
                    "source": path.name,
                    "headings": " > ".join(chunk.meta.headings or []),
                }
            )

        collection.upsert(ids=ids, documents=texts, metadatas=metadatas)
        print(
            f"{path.name}: {len(chunks)} chunks, "
            f"{len(doc.tables)} tables, "
            f"{sum(1 for t in doc.texts if t.label == 'section_header')} headings"
        )


if __name__ == "__main__":
    ingest([Path(p) for p in sys.argv[1:]])
