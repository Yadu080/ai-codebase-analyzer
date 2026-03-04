from fastapi import FastAPI
from pydantic import BaseModel

from app.repo_loader import clone_repository
from app.code_parser import load_code_files
from app.chunker import chunk_code
from app.embedder import embed_chunks, embed_query
from app.vector_store import build_index
from app.retriever import retrieve
from app.qa_engine import generate_answer
from app.architecture import build_dependency_graph
from app.repo_summary import generate_repo_summary

app = FastAPI()

class RepoRequest(BaseModel):
    repo_url: str

class QuestionRequest(BaseModel):
    question: str

pipeline = {}

@app.post("/analyze")

def analyze_repo(request: RepoRequest):

    repo_path = clone_repository(request.repo_url)

    files = load_code_files(repo_path)

    chunks = chunk_code(files)

    embeddings = embed_chunks(chunks)

    index = build_index(embeddings)

    pipeline["chunks"] = chunks
    pipeline["index"] = index

    summary = generate_repo_summary(repo_path, chunks)

    pipeline["summary"] = summary

    return {
    "message": "Repository indexed successfully",
    "chunks": len(chunks),
    "summary": summary
    }


@app.post("/ask")

def ask_question(request: QuestionRequest):

    query_embedding = embed_query(request.question)

    retrieved = retrieve(
        pipeline["index"],
        query_embedding,
        pipeline["chunks"]
    )

    answer = generate_answer(request.question,retrieved)

    return {"answer":answer}

@app.post("/architecture")

def architecture(request: RepoRequest):

    repo_path = clone_repository(request.repo_url)

    graph = build_dependency_graph(repo_path)

    return {"architecture": graph}
