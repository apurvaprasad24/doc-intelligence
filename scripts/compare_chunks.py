import sys

sys.path.insert(0, "src")

from docint.chunking import chunk_pages
from docint.pdf_loader import read_pdf_file
from docint.vector_store import build_index, search

PDF_PATH = "data/sample_docs/pdf1.pdf"  # your real file name

QUESTIONS = [
    "Define quantum mechanics",
    "Give a one line conclusion of the whole research"
    # TODO: add a second question here, in your own words (see Step 2)
]

CONFIGS = [
    (200, 40),
    (800, 150),
    (1500, 250),
]

pdf = read_pdf_file(PDF_PATH)

for chunk_size, overlap in CONFIGS:
    chunks = chunk_pages(pdf, chunk_size, overlap)
    index = build_index(chunks)
    print(f"\n===== chunk_size={chunk_size}, overlap={overlap}: {len(chunks)} chunks =====")

    for question in QUESTIONS:
        print(f"\nQ: {question}")
        for chunk, score in search(index, chunks, question, k=3):
            preview = chunk.text[:90].replace("\n", " ")
            print(f"  {score:.3f}  page {chunk.page_number}  {preview}")