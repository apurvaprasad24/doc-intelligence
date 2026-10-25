import numpy as np

from docint.embeddings import embed_texts


def test_embed_texts_shape_and_type():
    vectors = embed_texts(["hello world", "quantum mechanics"])

    assert vectors.shape == (2, 384)
    assert vectors.dtype == np.float32


def test_vectors_are_normalized():
    vectors = embed_texts(["hello world"])

    assert abs(float(np.linalg.norm(vectors[0])) - 1.0) < 1e-4