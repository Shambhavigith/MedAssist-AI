---
title: MedAssist AI
emoji: 🏥
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# MedAssist AI

An AI-powered medical information assistant built using Retrieval-Augmented Generation (RAG), FAISS vector search, LangChain, and Google Gemini.

🚀 **Live Demo:** https://shambhavii9-medassist-ai.hf.space

📂 **GitHub Repository:** https://github.com/Shambhavigith/MedAssist-AI

---

## Overview

MedAssist AI combines medical guideline documents and structured clinical disease datasets with semantic search and large language models to provide context-aware medical information.

The system retrieves relevant medical knowledge from a FAISS vector database before generating responses with Google Gemini, helping ground answers in the available knowledge base.

> 🚧 Project currently under active development. Prompt engineering, retrieval quality, UI/UX, and additional medical knowledge integrations are actively being improved.

---

## Tech Stack

### AI & Retrieval

* Google Gemini
* LangChain
* FAISS
* Hugging Face Embeddings
* Sentence Transformers (all-MiniLM-L6-v2)

### Backend

* Python
* Flask

### Data Sources

* Medical Guideline PDFs
* Clinical Disease Datasets
* Disease Descriptions
* Medications
* Diet Recommendations
* Workout Recommendations
* Precautions

---

## Architecture

```text
User Query
     ↓
Embedding-based Retrieval
     ↓
FAISS Vector Search
     ↓
Top-K Relevant Documents
     ↓
Prompt Construction
     ↓
Google Gemini
     ↓
Response Generation
```

## Current Status

### Completed

✅ Clinical Dataset Engineering
✅ Disease Knowledge Integration
✅ PDF Ingestion Pipeline
✅ FAISS Vector Store Creation
✅ Retrieval Pipeline
✅ Prompt Engineering
✅ nd-to-End RAG Integration
✅ Gemini API Integration
✅ Hugging Face Deployment

### In Progress


* UI Improvements
* Response Evaluation

### Planned

* Symptom-Based Disease Enrichment
* Source Citations
* Conversation Memory
* Enhanced User Experience

---

## Running Locally

```bash
pip install -r requirements.txt
python src/ingest.py
python app.py
```

---

## Disclaimer

This project is intended for educational and informational purposes only.

It is **not** a substitute for professional medical advice, diagnosis, or treatment. Users should always consult qualified healthcare professionals for medical decisions.

The project retrieves information from publicly available medical guidelines and clinical datasets. The respective copyrights and intellectual property remain with their original owners.

The developer does not claim ownership of third-party medical publications or guideline documents used for experimentation.

---

## Author

Shambhavi Singh

GitHub: https://github.com/Shambhavigith
