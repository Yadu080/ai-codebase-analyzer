def chunk_code(code_files, chunk_size=500):

    chunks = []

    for file in code_files:

        text = file["content"]
        path = file["file_path"]

        for i in range(0,len(text),chunk_size):

            chunks.append({
                "file_path": path,
                "chunk": text[i:i+chunk_size]
            })

    return chunks