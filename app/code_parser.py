import os

SUPPORTED_EXTENSIONS = [".py", ".js", ".ts", ".java", ".cpp", ".c"]

def load_code_files(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):

                file_path = os.path.join(root,file)

                try:
                    with open(file_path,"r",encoding="utf-8") as f:
                        content = f.read()

                    code_files.append({
                        "file_path": file_path,
                        "content": content
                    })

                except:
                    continue

    return code_files