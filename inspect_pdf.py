
from pathlib import Path

from docint.pdf_loader import read_pdf_file


pdf_path = Path("sample.pdf")

result = read_pdf_file(pdf_path)

print(f"Filename: {result.filename}")
print(f"Page count: {len(result.pages)}")

for page in result.pages:
    print(f"\n--- Page {page.page_number} ---")
    print(repr(page.text[:100]))
