import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

_model = None


def get_model() -> SentenceTransformer:
    """Load the model once, then reuse it (loading takes a few seconds)."""
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def embed_texts(texts: list[str]) -> np.ndarray:
    """Turn a list of texts into a (len(texts), 384) array of vectors."""
    # TODO: return the model's encode(...) of texts, with
    #   normalize_embeddings=True
    # then convert the result to float32 with .astype("float32")
    # (FAISS needs float32).
    return get_model().encode(texts, normalize_embeddings=True).astype("float32")