class ChunkingStrategies:
    @staticmethod
    def fixed_size_chunking(text: str,chunk_size: int=500,overlap: int=50) -> list:
        chunks=[]
        for i in range(0,len(text),chunk_size-overlap):
            chunk = text[i : i + chunk_size]
            chunks.append(chunk)
        return chunks
    @staticmethod
    def title_chain_prefix_chunking(elements: list) -> list:
        base_chunks = ChunkingStrategies.structure_aware_chunking(elements)
        tcp_chunks = []
        for chunk in base_chunks:
            prefix = f"[Section: {chunk['section']}]\n"
            tcp_chunks.append({
                "text": prefix + chunk["text"],
                "section": chunk["section"]
            })
        return tcp_chunks
    @staticmethod
    def recursive_chunking(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
        # Simple recursive approach by splitting paragraphs and combining up to chunk_size
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""
        for para in paragraphs:
            if len(current_chunk) + len(para) <= chunk_size:
                current_chunk += "\n\n" + para if current_chunk else para
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = para
        if current_chunk:
            chunks.append(current_chunk)
        return chunks
    @staticmethod
    def structure_aware_chunking(elements: list) -> list:
        chunks = []
        current_chunk = ""
        current_section = ""
        
        for el in elements:
            # If section changes or chunk gets too big, start a new chunk
            if el.get("section") != current_section or len(current_chunk) > 500:
                if current_chunk:
                    chunks.append({"text": current_chunk, "section": current_section})
                current_chunk = el.get("text", "")
                current_section = el.get("section", "General")
            else:
                current_chunk += " " + el.get("text", "")
        if current_chunk:
            chunks.append({"text": current_chunk, "section": current_section})
        return chunks


