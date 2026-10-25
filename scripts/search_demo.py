import sys

sys.path.insert(0, "src")

from docint.chunking import chunk_pages
from docint.pdf_loader import read_pdf_file
from docint.vector_store import build_index, search

PDF_PATH = "data/sample_docs/pdf1.pdf"  # change to your real file name
QUESTION = "Define quantum mechanics"

pdf = read_pdf_file(PDF_PATH)
chunks = chunk_pages(pdf)
print(f"{len(pdf.pages)} pages -> {len(chunks)} chunks")

index = build_index(chunks)

for chunk, score in search(index, chunks, QUESTION, k=3):
    print(f"\nscore={score:.3f}  {chunk.doc_name}  page {chunk.page_number}")
    print(chunk.text[:200].replace("\n", " "))