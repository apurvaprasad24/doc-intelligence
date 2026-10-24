# RAG Document Intelligence System

A hands-on AI engineering project to build a Retrieval-Augmented Generation (RAG) system that answers questions about uploaded documents using relevant retrieved passages and source citations.

The project is being developed incrementally to explore document processing, text chunking, embeddings, vector search, local LLMs, testing, and API development.

## Prerequisites

- Python 3.11 or 3.12
- VS Code
- Git (optional)

## Setup

Clone the repository or open the project directory, then create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked by your execution policy, you can run Python directly using `.venv\Scripts\python.exe` instead.

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install project dependencies if a `requirements.txt` file is available:

```powershell
python -m pip install -r requirements.txt
```

## Running Tests

Install pytest if it is not already installed:

```powershell
python -m pip install pytest
```

Run the test suite from the project root:

```powershell
python -m pytest
```

To see individual test names and results:

```powershell
python -m pytest -v
```

## Project Structure

```text
rag-document-intelligence/
├── data/
│   └── sample.txt
├── src/
│   └── inspect_document.py
├── tests/
├── .venv/
├── requirements.txt
└── README.md
```

The `tests/` directory will contain automated tests as the project grows. The `.venv/` directory contains the local Python environment and should not be committed to Git.

## Development Goal

Build a working document question-answering system step by step, with an emphasis on understanding the implementation, testing individual components, and learning practical AI engineering.
