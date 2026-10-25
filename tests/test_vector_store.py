import pytest

from docint.chunking import Chunk
from docint.vector_store import build_index, search


def make_chunks():
    texts = [
        "Cats are small furry animals that purr and chase mice.",
        "The stock market fell sharply after the interest rate decision.",
        "Photosynthesis lets plants turn sunlight into chemical energy.",
    ]
    return [
        Chunk(doc_name="demo.pdf", page_number=i + 1, chunk_index=0, text=t)
        for i, t in enumerate(texts)
    ]


def test_search_returns_the_most_relevant_chunk():
    chunks = make_chunks()
    index = build_index(chunks)

    results = search(index, chunks, "Which animal likes to catch mice?", k=1)

    top_chunk, score = results[0]
    assert top_chunk.page_number == 1


def test_build_index_rejects_empty_list():
    with pytest.raises(ValueError):
        build_index([])


def test_search_with_k_larger_than_chunk_count():
    chunks = make_chunks()
    index = build_index(chunks)

    results = search(index, chunks, "plants and sunlight", k=10)

    assert len(results) == 3