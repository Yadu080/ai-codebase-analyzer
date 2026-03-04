def retrieve(index, query_embedding, chunks, top_k=5):

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results