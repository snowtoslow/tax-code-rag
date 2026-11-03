"""Parse a PDF, chunk it with Docling, and index the chunks in Chroma."""

import sys
from pathlib import Path

import chromadb
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter


def ingest(source: str, collection_name: str = "docs") -> None:
    doc = DocumentConverter().convert(source).document

    chunker = HybridChunker()
    chunks = list(chunker.chunk(dl_doc=doc))

    ids, texts, metadatas = [], [], []
    for i, chunk in enumerate(chunks):
        # contextualize() prepends headings, which improves retrieval quality
        text = chunker.contextualize(chunk=chunk)

        pages = sorted(
            {
                prov.page_no
                for item in chunk.meta.doc_items
                for prov in item.prov
            }
        )
        ids.append(f"{Path(source).stem}-{i}")
        texts.append(text)
        metadatas.append(
            {
                "source": source,
                "headings": " > ".join(chunk.meta.headings or []),
                "page": pages[0] if pages else -1,
            }
        )

    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(collection_name)
    collection.upsert(ids=ids, documents=texts, metadatas=metadatas)
    print(f"Indexed {len(chunks)} chunks from {source}")


if __name__ == "__main__":
    ingest(sys.argv[1])