from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):

    texts = [c["chunk"] for c in chunks]

    embeddings = model.encode(texts)

    return embeddings


def embed_query(query):

    return model.encode([query])