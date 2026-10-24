
import pytest
import pymupdf

from docint.pdf_loader import read_pdf_file


def create_pdf(path, page_texts):
    """Create a PDF with the supplied text on each page."""
    doc = pymupdf.open()

    try:
        for text in page_texts:
            page = doc.new_page()

            if text:
                page.insert_text((72, 72), text)

        doc.save(str(path))
    finally:
        doc.close()


def test_extracts_text_from_three_pages(tmp_path):
    pdf_path = tmp_path / "three_pages.pdf"

    create_pdf(
        pdf_path,
        [
            "Introduction to RAG",
            "Document retrieval",
            "Answer generation",
        ],
    )

    result = read_pdf_file(pdf_path)

    assert result.filename == "three_pages.pdf"
    assert len(result.pages) == 3

    assert [page.page_number for page in result.pages] == [1, 2, 3]

    assert result.pages[0].text.strip() == "Introduction to RAG"
    assert result.pages[1].text.strip() == "Document retrieval"
    assert result.pages[2].text.strip() == "Answer generation"


def test_rejects_fake_pdf(tmp_path):
    fake_pdf = tmp_path / "fake.pdf"
    fake_pdf.write_text("This is not a real PDF", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid PDF file"):
        read_pdf_file(fake_pdf)


def test_rejects_pdf_with_all_blank_pages(tmp_path):
    pdf_path = tmp_path / "blank.pdf"
    create_pdf(pdf_path, ["", "", ""])

    with pytest.raises(ValueError, match="No extractable text"):
        read_pdf_file(pdf_path)


def test_preserves_blank_page_in_middle(tmp_path):
    pdf_path = tmp_path / "middle_blank.pdf"

    create_pdf(
        pdf_path,
        ["First page has text", "", "Third page has text"],
    )

    result = read_pdf_file(pdf_path)

    assert len(result.pages) == 3
    assert result.pages[0].page_number == 1
    assert result.pages[1].page_number == 2
    assert result.pages[2].page_number == 3

    assert "First page has text" in result.pages[0].text
    assert result.pages[1].text.strip() == ""
    assert "Third page has text" in result.pages[2].text


def test_missing_file(tmp_path):
    missing_path = tmp_path / "missing.pdf"

    with pytest.raises(FileNotFoundError, match="File not found"):
        read_pdf_file(missing_path)


def test_rejects_wrong_extension(tmp_path):
    txt_path = tmp_path / "notes.txt"
    txt_path.write_text("Some text", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported file extension"):
        read_pdf_file(txt_path)


def test_rejects_directory(tmp_path):
    directory = tmp_path / "folder.pdf"
    directory.mkdir()

    with pytest.raises(ValueError, match="Path is not a file"):
        read_pdf_file(directory)


def test_rejects_encrypted_pdf(tmp_path):
    pdf_path = tmp_path / "encrypted.pdf"
    doc = pymupdf.open()

    try:
        page = doc.new_page()
        page.insert_text((72, 72), "Protected content")

        doc.save(
            str(pdf_path),
            encryption=pymupdf.PDF_ENCRYPT_AES_256,
            owner_pw="owner-secret",
            user_pw="user-secret",
        )
    finally:
        doc.close()

    with pytest.raises(ValueError, match="Encrypted PDF"):
        read_pdf_file(pdf_path)
