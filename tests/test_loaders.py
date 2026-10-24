import pytest
from docint.loaders import read_text_file
from pathlib import Path

def test_reads_valid_text_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Hello, RAG!", encoding="utf-8")

    result = read_text_file(file)

    assert result.text == "Hello, RAG!"
    assert result.filename == "sample.txt"
    assert result.char_count == len("Hello, RAG!")


def test_missing_file_raises_file_not_found(tmp_path):
    missing = tmp_path / "does_not_exist.txt"

    with pytest.raises(FileNotFoundError):
        read_text_file(missing)


def test_folder_named_like_txt_file_raises_value_error(tmp_path):
    folder = tmp_path / "notes.txt"
    folder.mkdir()

    with pytest.raises(ValueError, match="not a file"):
        read_text_file(folder)

def test_wrong_extension_raises_value_error(tmp_path):
    file = tmp_path / "report.pdf"
    file.write_text("some content", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid file extension"):
        read_text_file(file)


def test_whitespace_only_file_raises_value_error(tmp_path):
    file = tmp_path / "blank.txt"
    file.write_text("   \n\n\t  ", encoding="utf-8")

    with pytest.raises(ValueError, match="empty or contains only whitespace"):
        read_text_file(file)

def test_invalid_utf8(tmp_path: Path):
    file = tmp_path / "invalid.txt"
    file.write_bytes(b"\xff\xfe\x00bad")

    with pytest.raises(
        ValueError,
        match="File is not valid UTF-8 text"
    ):
        read_text_file(file)