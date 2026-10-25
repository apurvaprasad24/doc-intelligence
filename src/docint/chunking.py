from dataclasses import dataclass

from docint.pdf_loader import PDFResult


@dataclass
class Chunk:
    doc_name: str
    page_number: int
    chunk_index: int
    text: str


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 150) -> list[str]:
    if chunk_size <= 0 or overlap < 0:
        raise ValueError("chunk_size must be positive and overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        chunk = text[start : start + chunk_size]
        chunks.append(chunk)
        if start + chunk_size >= len(text):
            break
        start += chunk_size - overlap

    return chunks


def chunk_pages(
    pdf: PDFResult, chunk_size: int = 800, overlap: int = 150
) -> list[Chunk]:
    chunks: list[Chunk] = []

    for page in pdf.pages:
        pieces = chunk_text(page.text, chunk_size, overlap)

        for i, piece in enumerate(pieces):
            chunks.append(
                Chunk(
                    doc_name=pdf.filename,
                    page_number=page.page_number,
                    chunk_index=i,
                    text=piece,
                )
            )

    return chunks
