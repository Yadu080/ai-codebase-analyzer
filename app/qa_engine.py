from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(question, retrieved_chunks):

    context = "\n\n".join(
        [f"File: {c['file_path']}\n{c['chunk']}" for c in retrieved_chunks]
    )

    prompt = f"""
You are a senior software engineer analyzing a GitHub repository.

Code Context:
{context}

Question:
{question}

Explain clearly which file or module handles this functionality.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return completion.choices[0].message.content