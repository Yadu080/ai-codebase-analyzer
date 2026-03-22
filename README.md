# AI Codebase Analyzer

AI Codebase Analyzer is a tool for exploring and understanding software repositories using Retrieval Augmented Generation (RAG).

The system analyzes a GitHub repository by cloning it, extracting source files, generating semantic embeddings for code chunks, and indexing them using FAISS. When a user asks a question, the system retrieves the most relevant code segments and provides an explanation using a language model.

This project demonstrates how vector search and language models can be combined to analyze and explain large codebases.

---

## Features

- Analyze any public GitHub repository
- Extract and process source code files
- Generate semantic embeddings for code
- Vector similarity search using FAISS
- Question answering about repository code
- Repository summary (languages, files, modules)
- Optional AST-based dependency analysis
- Web interface built with Streamlit

---

## System Architecture

The system consists of three main layers:

Frontend  
Streamlit interface for interacting with the system.

Backend  
FastAPI service responsible for repository processing, vector indexing, and answering questions.

AI Pipeline  
A Retrieval Augmented Generation (RAG) pipeline that retrieves relevant code context before generating responses.

---

## Architecture Diagram

```
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Repository Loader
 ├── Code Parser
 ├── Code Chunker
 ├── Embedding Generator
 │
 ▼
FAISS Vector Index
 │
 ▼
Retriever
 │
 ▼
LLM (Groq API)
 │
 ▼
Generated Explanation
```

---

## RAG Pipeline

The question answering process uses a Retrieval Augmented Generation architecture.

```
User Question
      │
      ▼
Embed Question
      │
      ▼
Vector Search (FAISS)
      │
      ▼
Retrieve Relevant Code Chunks
      │
      ▼
Send Context + Question to LLM
      │
      ▼
Generate Answer
```

This approach ensures the language model answers using actual code from the repository.

---

## Repository Processing Pipeline

When a repository is analyzed, the system performs the following steps:

```
GitHub Repository URL
        │
        ▼
Clone Repository
        │
        ▼
Load Source Files
        │
        ▼
Chunk Code into Segments
        │
        ▼
Generate Embeddings
        │
        ▼
Store Embeddings in FAISS Index
        │
        ▼
Repository Ready for Queries
```

---

## Architecture Analysis

The project also includes a static analysis component using Python AST.

```
Python Files
      │
      ▼
AST Parsing
      │
      ▼
Extract Import Relationships
      │
      ▼
Build Dependency Graph
```

This provides a high-level view of how modules in the repository interact.

---

## Project Structure

```
ai-codebase-analyzer
│
├── app
│   ├── repo_loader.py
│   ├── code_parser.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── qa_engine.py
│   ├── repo_summary.py
│   ├── architecture.py
│   └── api.py
│
├── data
│
├── frontend.py
├── requirements.txt
├── run.sh
├── .gitignore
└── .env
```

---

## Setup

Clone the repository and install dependencies.

```
git clone <repository_url>
cd ai-codebase-analyzer
pip install -r requirements.txt
```

Create a `.env` file containing your Groq API key.

```
GROQ_API_KEY=your_api_key
```

---

## Running the Application

You can start both backend and frontend with a single command:

```
./run.sh
```

Or run them separately.

Start the backend:

```
uvicorn app.api:app --reload
```

Start the frontend:

```
streamlit run frontend.py
```

The Streamlit interface will open in your browser.

---

## Screenshot

[![Screenshot-2026-03-04-at-10-22-45-PM.png](https://i.postimg.cc/7hbnpZPf/Screenshot-2026-03-04-at-10-22-45-PM.png)](https://postimg.cc/xNDmmYz2)


## Example Usage

1. Enter a GitHub repository URL
2. Click **Analyze Repository**
3. Ask questions about the codebase

Example questions:

- How does routing work in this project?
- Where is authentication implemented?
- What modules are responsible for handling requests?

---

## Technologies Used

Backend
- FastAPI
- Python

Vector Search
- FAISS

Embeddings
- SentenceTransformers

Language Model
- Groq API

Frontend
- Streamlit

Static Analysis
- Python AST

---

## Limitations

- The vector index is stored in memory, so restarting the server requires re-indexing the repository.
- The system currently focuses on Python repositories for best results.

---

## Purpose

This project is intended as a demonstration of how Retrieval Augmented Generation can be applied to source code analysis and developer tooling.
