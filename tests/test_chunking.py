import pytest
from docint.chunking import chunk_text
from docint.chunking import chunk_pages
from docint.pdf_loader import PDFResult, PageResult

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

def test_chunk_pages_keeps_page_numbers():
    pdf = PDFResult(
        filename="demo.pdf",
        pages=[
            PageResult(text="A" * 25, page_number=1),
            PageResult(text="", page_number=2),
            PageResult(text="B" * 5, page_number=3),
        ],
    )

    chunks = chunk_pages(pdf, chunk_size=10, overlap=3)

    assert all(c.doc_name == "demo.pdf" for c in chunks)
    assert {c.page_number for c in chunks} == {1, 3}
    assert all(set(c.text) == {"A"} for c in chunks if c.page_number == 1)
    assert all(set(c.text) == {"B"} for c in chunks if c.page_number == 3)