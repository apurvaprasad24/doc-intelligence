
from dataclasses import dataclass
from pathlib import Path

import pymupdf

@dataclass
class Chunk:
    doc_name: str
    page_number: int
    chunk_index: int
    text: str

@dataclass
class PageResult:
    text: str
    page_number: int


@dataclass
class PDFResult:
    filename: str
    pages: list[PageResult]


def read_pdf_file(path: str | Path) -> PDFResult:
    """Extract text from a PDF while preserving its page numbers."""

    file_path = Path(path)

    # 1. Check whether the file exists.
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # 2. Check whether the path points to a file.
    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    # 3. Check the file extension.
    if file_path.suffix.lower() != ".pdf":
        raise ValueError(
            f"Unsupported file extension: {file_path.suffix}. "
            "Expected a .pdf file."
        )

    doc = None

    try:
        # 4. Open and validate the PDF.
        try:
            doc = pymupdf.open(str(file_path))
        except pymupdf.FileDataError as exc:
            raise ValueError(
                f"Invalid PDF file: {file_path}"
            ) from exc

        # 5. Reject password-protected PDFs.
        if doc.is_encrypted or doc.needs_pass:
            raise ValueError(
                f"Encrypted PDF is not supported: {file_path}"
            )

        # 6. Extract text from each page.
        pages: list[PageResult] = []

        for index in range(doc.page_count):
            page = doc.load_page(index)
            text = page.get_text()

            pages.append(
                PageResult(
                    text=text,
                    page_number=index + 1,
                )
            )

        # 7. Reject PDFs with no extractable text anywhere.
        if not any(page.text.strip() for page in pages):
            raise ValueError(
                f"No extractable text found in PDF: {file_path}"
            )

        # 8. Return the structured result.
        return PDFResult(
            filename=file_path.name,
            pages=pages,
        )

    finally:
        # Close the document even if extraction or validation fails.
        if doc is not None:
            doc.close()

