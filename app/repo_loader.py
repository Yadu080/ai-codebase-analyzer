import git
import os

def clone_repository(repo_url, save_dir="data"):

    repo_name = repo_url.split("/")[-1].replace(".git","")
    repo_path = os.path.join(save_dir, repo_name)

    if os.path.exists(repo_path):
        print("Repository already exists.")
        return repo_path

    print("Cloning repository...")
    git.Repo.clone_from(repo_url, repo_path)
    print("Repository cloned.")

    return repo_path