# docling-pdf

A small Retrieval-Augmented Generation (RAG) project that answers questions about PDF documents.

1. **Parse** a PDF with [Docling](https://github.com/docling-project/docling)
2. **Chunk** it with Docling's structure-aware `HybridChunker`
3. **Index** the chunks in a local [Chroma](https://www.trychroma.com/) vector database
4. **Retrieve** the chunks most relevant to a question
5. **Generate** an answer with Google Gemini, with citations to the source chunks

Everything except the final answer generation runs locally.

## Requirements

- [uv](https://docs.astral.sh/uv/) (Python package and project manager)
- Python 3.10-3.13 (the project pins **3.12**; uv downloads it automatically if needed)
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- Roughly 5 GB of free disk space (Docling pulls in PyTorch and downloads ML models on first run)

> **Note:** Avoid Python 3.14+ for now. Some dependencies (such as `chromadb`) may not have compatible builds yet, and uv can silently fall back to a very old, broken version.

## Download

Sample documents and any other files needed to try the project:

**Download URL:** `https://www.legis.md/cautare/getResults?doc_id=79111&lang=ro`

```bash
# Example: download a sample PDF into the input/ folder
mkdir -p input
mv donwloaded_file.pdf input
```

## Getting started

### 1. Install dependencies

```bash
uv sync
```

This creates a `.venv` using the Python version from `.python-version` and installs everything from `uv.lock`.

### 2. Configure environment variables

Copy the template and fill in your key:

```bash
cp .env.example .env
```

```env
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.5-flash
GEMINI_FALLBACK_MODEL=gemini-2.5-flash-lite
```

| Variable | Description |
| --- | --- |
| `GEMINI_API_KEY` | Your Google AI Studio API key (required) |
| `GEMINI_MODEL` | Primary model used for answers (required) |
| `GEMINI_FALLBACK_MODEL` | Used if the primary model is overloaded (required) |
| `HF_TOKEN` | Optional. Hugging Face read token for faster first-time model downloads |

Model names change over time. To list the models available to your key:

```bash
uv run python -c "from google import genai; [print(m.name) for m in genai.Client().models.list()]"
```

`.env` is gitignored. Never commit your API key.

## Usage

### Multilingual HTML retrieval

HTML ingestion and querying use `BAAI/bge-m3` through Sentence Transformers,
with normalized embeddings and a separate `docs_bge_m3` collection. The original
`docs` collection is preserved. The PDF ingestion script still uses the original
collection; the query script now targets the multilingual HTML collection.

Install the added dependency and rebuild the HTML index before querying:

```bash
uv sync
CHROMA_PATH=src/docling_pdf/chroma_db_html uv run python -m docling_pdf.ingest_html input/page.html
CHROMA_PATH=src/docling_pdf/chroma_db_html uv run python -m docling_pdf.query "Care este poziția tarifară a caviarului?"
```

Run these commands from the project root. The first embedding operation downloads
the model; BGE-M3 uses more memory and processing time than the original MiniLM
model. Querying before re-ingestion will fail because the new collection does
not exist yet. The dependency lockfile must be refreshed by `uv sync`.

This change uses BGE-M3's dense embeddings only. Table chunking is unchanged;
retrieval quality still needs to be checked against representative questions.

### Ingest a PDF

Parses the document, chunks it, and stores the chunks in `chroma_db/`:

```bash
uv run python -m docling_pdf.ingest input/sample.pdf
```

Quote paths that contain spaces. To ingest several files:

```bash
for f in input/*.pdf; do uv run python -m docling_pdf.ingest "$f"; done
```

Re-running on the same file updates existing chunks instead of duplicating them.

### Ask a question

```bash
uv run python -m docling_pdf.query "What does the document say about ...?"
```

The answer is generated from the retrieved chunks and cites its sources as `[1]`, `[2]`, and so on, each with a page number and section heading.

## First run

The first run is slow. Expect these one-time downloads, which are cached afterwards:

- Docling layout and table-structure models (from Hugging Face)
- Chroma's default embedding model (`all-MiniLM-L6-v2`)

A warning about unauthenticated Hugging Face requests is harmless. Set `HF_TOKEN` to silence it and speed up downloads.

## Project structure

```
docling-pdf/
├── src/docling_pdf/
    ├── chroma_db/         # local vector store (gitignored, rebuilt by ingest)
│   ├── __init__.py
│   ├── ingest.py      # parse -> chunk -> embed -> store
│   └── query.py       # retrieve -> generate
├── input/             # your PDFs (gitignored)
├── .env               # secrets (gitignored)
├── .env.example       # template for .env
├── .python-version
├── pyproject.toml
└── uv.lock
```

## Troubleshooting

```bash
uv python pin 3.12
rm -rf .venv uv.lock
uv sync
```

## Development notes

- Commit `pyproject.toml`, `uv.lock`, and `.python-version`. Do not commit `.env`, `chroma_db/`, or private PDFs.
- Add dependencies with `uv add <package>` and dev-only tools with `uv add --dev <package>`.
- Chroma's default embedding model is English-focused. For non-English documents (for example Romanian), consider a multilingual embedder such as `bge-m3` or `multilingual-e5`, then re-ingest, because vectors from different models are not compatible.

- Script for good display download:
```js
const html = document.querySelector("div.docx").outerHTML;
const blob = new Blob([html], { type: "text/html;charset=utf-8" });
const url = URL.createObjectURL(blob);

const a = document.createElement("a");
a.href = url;
a.download = "page.html";
a.click();

URL.revokeObjectURL(url);
```

- Python script for running ingestion using ingest_html.py 
```python
    uv run ingest_html.py /Users/snowtoslow/Desktop/projects/docling-pdf/input/page.html
```

### Observations:
1. PDF vs HTML source(HTML MUCH BETTER, BECAUSE IT PRESERVES THE TABLE STRUCTURE WHICH WAS A MESS WITH PDF)
2. EMBEDDING MODEL SELECTION 
   * The chromadb embedding model set by default all-MiniLM-L6-v2 produces 
     384-dimensional vectors and is primarily English-focused; (ingestion result: Indexed 1911 chunks from tax-code.pdf)
   * Fine tunned it to BAAI/bge-m3 which works better in multilingual environment (ingestion result: page.html: 1925 chunks, 11 tables, 5 headings)
   


### Questions: 
1. uv run query.py "Care este poziția tarifară a caviarului?" => was ok on initial setup
2. uv run query.py "Care este cota accizelor pentru caviar in anul 2026?" => 1024 tokens