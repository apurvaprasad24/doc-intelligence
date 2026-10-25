from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The cat sat on the mat.",
    "A kitten is resting on a rug.",
    "Quarterly revenue grew by 12 percent.",
]

vectors = model.encode(sentences, normalize_embeddings=True)
print("shape:", vectors.shape)

print("cat vs kitten:", vectors[0] @ vectors[1])
print("cat vs revenue:", vectors[0] @ vectors[2])