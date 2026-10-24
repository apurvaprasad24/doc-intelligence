from pathlib import Path
from dataclasses import dataclass

@dataclass
class FileResult:
    text :str
    filename : str 
    char_count : int 

def  read_text_file(path:str | Path) -> FileResult:
    path =Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"File not found: '{path}'"
        )
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: '{path}'")
    
    if path.suffix.lower() != ".txt":
        raise ValueError(
            f"Invalid file extension: expected '.txt',"
            f"got '{path.suffix or '(no extension)'}'"
        )
    
    try:
     text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(
            f"File is not valid UTF-8 text: '{path.name}'"
        ) from exc

    if not text.strip():
        raise ValueError(
            f"File is empty or contains only whitespace: '{path.name}'"
        )
    
    return FileResult(
        text=text,
        filename=path.name,
        char_count=len(text)
    )