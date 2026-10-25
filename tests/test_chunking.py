import pytest
from docint.chunking import chunk_text


def test_example_from_lesson():
    assert chunk_text("ABCDEFGHIJKLMNOPQRST", chunk_size=10, overlap=3) == [
        "ABCDEFGHIJ",
        "HIJKLMNOPQ",
        "OPQRST",
    ]


def test_empty_text_returns_empty_list():
    assert chunk_text("") == []


def test_overlap_too_big_raises():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=5, overlap=5)

def test_no_redundant_last_chunk():
    assert chunk_text("ABCDEFGHIJKLMNOPQ", chunk_size=10, overlap=3) == [
        "ABCDEFGHIJ",
        "HIJKLMNOPQ",
    ]

def test_invalid_sizes_raise():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=0, overlap=0)
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=5, overlap=-1)