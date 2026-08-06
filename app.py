import streamlit as st
import tempfile
import os

# Import our custom modules from the src folder
from src.parser import DocumentParser
from src.chunkers import ChunkingStrategies
from src.retriever import RAGRetriever

# Set up Streamlit page configuration
st.set_page_config(page_title="TitleChainRAG Benchmark", layout="wide")

st.title("TitleChainRAG: Structure-Aware Chunking Evaluation Dashboard")
st.markdown("Compare retrieval effectiveness side-by-side across **Fixed-size, Recursive, Structure-Aware, and Title-Chain Prefix (TCP)** chunking strategies.")

# 1. File Uploader for PDF
uploaded_file = st.file_uploader("Upload a research paper or PDF document", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded PDF temporarily so PyMuPDF can read it
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    st.success("PDF uploaded successfully! Processing document...")

    # 2. Parse the PDF
    parser = DocumentParser(tmp_path)
    elements = parser.extract_structured_elements()
    
    # Flatten elements into plain text for standard chunkers
    full_text = " ".join([e if isinstance(e, str) else e.get("text", "") for e in elements])

    # 3. Generate chunks using our different strategies
    fixed_chunks = ChunkingStrategies.fixed_size_chunking(full_text)
    recursive_chunks = ChunkingStrategies.recursive_chunking(full_text)
    
    # Format elements for structure-aware chunking if parser returned strings
    structured_elements = [{"text": e, "section": "General"} if isinstance(e, str) else e for e in elements]
    struct_chunks = ChunkingStrategies.structure_aware_chunking(structured_elements)
    tcp_chunks = ChunkingStrategies.title_chain_prefix_chunking(structured_elements)

    # 4. Search query input
    query = st.text_input("Enter your retrieval question:", "What are the main findings of this document?")

    if st.button("Run Retrieval Comparison"):
        strategies = {
            "Fixed-size": fixed_chunks,
            "Recursive": recursive_chunks,
            "Structure-Aware": struct_chunks,
            "Title-Chain Prefix (TCP)": tcp_chunks
        }

        # Create side-by-side columns for each strategy
        cols = st.columns(len(strategies))
        
        for col, (name, chunks) in zip(cols, strategies.items()):
            with col:
                st.subheader(name)
                
                # Build retriever index for this specific strategy
                retriever = RAGRetriever()
                retriever.build_index(chunks)
                
                # Retrieve top 3 results
                results = retriever.retrieve(query, k=3)
                
                for idx, res in enumerate(results, 1):
                    st.markdown(f"**Rank {idx}** (Score: {res['score']:.3f})")
                    st.info(res['text'][:300] + "...")
