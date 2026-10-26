
# AI API Testing Agent

An intelligent REST API testing platform using Generative AI,
RAG, and multi-agent systems.

## Project Overview

This project aims to automate REST API test generation,
execution, and analysis using Large Language Models.

The system will support:
- Local LLMs (Ollama / Qwen)
- Cloud LLMs (OpenAI API)
- LangChain and LangGraph
- Retrieval-Augmented Generation (RAG)
- Fine-tuning experiments
- Comparative evaluation of LLM performance

## Current Status

### Phase 1 — REST API & Automated Testing (Completed)

- REST API developed with FastAPI
- Interactive Swagger/OpenAPI documentation
- User management endpoints
- Input validation with Pydantic
- Automated tests using Pytest
- 5 tests passing

### Phase 2 — Local LLM Integration (Next)

- Ollama setup
- Qwen model integration
- LangChain integration
- First AI-generated test scenarios

## Tech Stack

**Backend:** Python, FastAPI, Pydantic

**Testing:** Pytest, FastAPI TestClient

**Planned AI:** LangChain, LangGraph, Ollama,
OpenAI API, RAG, Hugging Face, LoRA/QLoRA

**Planned Frontend:** Next.js, TypeScript

## Installation

### 1. Clone repository

```bash
git clone https://github.com/yesminedjebbi/ai-api-testing-agent.git
cd ai-api-testing-agent/backend
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell, activate with:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the API

```bash
python -m uvicorn app.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

### 5. Run tests

```bash
python -m pytest tests/ -v
```

## Roadmap

- [x] Phase 1: FastAPI & Pytest
- [ ] Phase 2: Local & Cloud LLMs
- [ ] Phase 3: AI Test Generation with LangChain
- [ ] Phase 4: RAG with FAISS or ChromaDB
- [ ] Phase 5: Multi-Agent System with LangGraph
- [ ] Phase 6: Next.js Frontend & PostgreSQL
- [ ] Phase 7: Fine-Tuning & Benchmarking
- [ ] Phase 8: Docker & CI/CD
