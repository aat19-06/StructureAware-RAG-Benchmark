# TitleChainRAG: Structure-Aware Semantic Chunking & Title-Chain Prefixes

![Python](https://img.shields.io/badge/Python-3.11%2B-blue )
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red )
![LangChain](https://img.shields.io/badge/LangChain-RAG-green )
![FAISS](https://img.shields.io/badge/FAISS-VectorSearch-orange )

Unlike standard PDF chat tutorials (`PDF → FAISS → Chatbot`), **TitleChainRAG** is a research-driven evaluation framework inspired by recent literature on **Structure-Aware Semantic Chunking with Title-Chain Prefixes (TCP)**. 

It implements, compares, and visualizes multiple chunking strategies side-by-side to solve context fragmentation in Retrieval-Augmented Generation (RAG).

---

## 🚀 Key Features

- **Multi-Strategy Chunking Pipeline**: Compares 4 distinct approaches:
  1. **Fixed-Size Chunking**: Rigid character slicing.
  2. **Recursive Chunking**: Paragraph/sentence-aware splitting.
  3. **Structure-Aware Chunking**: Section-boundary preserving chunking.
  4. **Title-Chain Prefix (TCP) Chunking**: Prepends hierarchical breadcrumbs (`[Section: ...]`) to preserve global context.
- **Hierarchical PDF Parsing**: Powered by PyMuPDF (`fitz`) to extract document titles, sections, and structural headers.
- **FAISS Vector Retrieval**: Embeds chunks using HuggingFace sentence transformers (`all-MiniLM-L6-v2`) for fast semantic similarity search.
- **Interactive Streamlit Dashboard**: A side-by-side visual comparison app that lets you upload any PDF and evaluate how different chunking strategies retrieve text for custom queries.

---

## 📁 Project Directory Structure

```text
TitleChainRAG/
│
├── data/                    # Sample PDFs (e.g., research papers)
├── src/
│   ├── __init__.py
│   ├── parser.py            # Hierarchical PDF parsing & section extraction
│   ├── chunkers.py          # Fixed, Recursive, Structure-Aware, & TCP chunking
│   └── retriever.py         # FAISS vector store & similarity search
│
├── app.py                   # Interactive Streamlit visual dashboard
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation 

## 🛠️ Quick Start & Installation
Clone the repository:
Bash
git clone https://github.com/YOUR_USERNAME/TitleChainRAG.git
cd TitleChainRAG
Install dependencies:
Bash
pip install -r requirements.txt
Run the Streamlit Dashboard:
Bash
streamlit run app.py
Test it out:
Open the local Streamlit URL in your browser.
Upload a structured PDF (like a research paper ).
Enter a deep technical query and compare how TCP and Structure-Aware chunking surface relevant context compared to standard fixed-size chunking.

## 📚 References & Research Background
This project is built as a reproduction and implementation study based on the following research paper:
Structure-Aware Semantic Chunking with Title-Chain Prefixes: A 1600-Query Evaluation and the Measurement Trap in Text-Transform Ablations
