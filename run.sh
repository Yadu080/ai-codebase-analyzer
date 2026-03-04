#!/bin/bash

echo "Starting backend..."
uvicorn app.api:app --reload &

echo "Starting frontend..."
streamlit run frontend.py