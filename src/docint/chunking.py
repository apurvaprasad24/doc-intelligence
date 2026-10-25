def chunk_text(text: str, chunk_size: int = 800, overlap: int = 150) -> list[str]:
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
