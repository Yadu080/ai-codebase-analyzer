import os
import ast

def build_dependency_graph(repo_path):

    graph = {}

    for root, _, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    source = f.read()

                try:
                    tree = ast.parse(source)
                except:
                    continue

                imports = []

                for node in ast.walk(tree):

                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            imports.append(alias.name)

                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            imports.append(node.module)

                graph[file] = imports

    return graph