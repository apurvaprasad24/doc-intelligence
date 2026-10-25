import faiss
from docint.config import TOP_K
from docint.chunking import Chunk
from docint.embeddings import embed_texts


def build_index(chunks: list[Chunk]) -> faiss.IndexFlatIP:
    """Embed every chunk and put the vectors in a FAISS index."""
    if not chunks:
        raise ValueError("Cannot build an index from zero chunks")

    vectors = embed_texts([c.text for c in chunks])
    index = faiss.IndexFlatIP(vectors.shape[1])  # 384 dimensions
    index.add(vectors)
    return index


def search(
    index: faiss.IndexFlatIP, chunks: list[Chunk], query: str, k: int = TOP_K
) -> list[tuple[Chunk, float]]:
    """Return the k chunks closest in meaning to the query, with scores."""
    query_vector = embed_texts([query])
    scores, ids = index.search(query_vector, k)

    results = []
    for score, i in zip(scores[0], ids[0]):
        if i == -1:  # FAISS pads with -1 when there are fewer than k chunks
            continue
        results.append((chunks[i], float(score)))
    return results