from dataclasses import dataclass

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
