import os

def generate_repo_summary(repo_path, chunks):

    total_files = 0
    languages = set()
    modules = []

    for root, _, files in os.walk(repo_path):

        for file in files:

            total_files += 1

            if file.endswith(".py"):
                languages.add("Python")

            if file.endswith(".js"):
                languages.add("JavaScript")

            if file.endswith(".ts"):
                languages.add("TypeScript")

            if file.endswith(".java"):
                languages.add("Java")

            if file.endswith(".py"):
                modules.append(file)

    summary = {
        "languages": list(languages),
        "main_modules": modules[:5],   # first few modules
        "total_files": total_files,
        "total_chunks": len(chunks)
    }

    return summary