"""
Advanced Document Chunking for RAG Systems
Supports semantic, recursive, and fixed-size chunking strategies.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import re
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter
)


class ChunkStrategy(Enum):
    """Available chunking strategies."""
    FIXED = "fixed"  # Fixed character/token size
    SEMANTIC = "semantic"  # Semantic boundaries (paragraphs, sentences)
    RECURSIVE = "recursive"  # Recursive splitting with multiple separators
    SLIDING_WINDOW = "sliding_window"  # Overlapping windows


@dataclass
class Chunk:
    """A document chunk with metadata."""
    content: str
    chunk_id: str
    document_id: str
    chunk_index: int
    metadata: Dict[str, Any]
    char_count: int
    token_count: Optional[int] = None

    def __post_init__(self):
        if self.char_count == 0:
            self.char_count = len(self.content)


class DocumentChunker:
    """Advanced document chunker with multiple strategies."""

    def __init__(
        self,
        strategy: ChunkStrategy = ChunkStrategy.RECURSIVE,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        separators: Optional[List[str]] = None
    ):
        """
        Initialize document chunker.

        Args:
            strategy: Chunking strategy to use
            chunk_size: Target chunk size (characters or tokens)
            chunk_overlap: Overlap between chunks
            separators: Custom separators for recursive splitting
        """
        self.strategy = strategy
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", ". ", " ", ""]

        self._init_splitter()

    def _init_splitter(self):
        """Initialize the appropriate text splitter."""
        if self.strategy == ChunkStrategy.RECURSIVE:
            self.splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                separators=self.separators,
                length_function=len
            )
        elif self.strategy == ChunkStrategy.FIXED:
            self.splitter = CharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                separator="\n"
            )
        elif self.strategy == ChunkStrategy.SEMANTIC:
            # For semantic chunking, we'll use custom logic
            self.splitter = None
        else:
            self.splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap
            )

    def chunk_document(
        self,
        text: str,
        document_id: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> List[Chunk]:
        """
        Chunk a document into smaller pieces.

        Args:
            text: Document text
            document_id: Unique document identifier
            metadata: Additional metadata

        Returns:
            List of Chunk objects
        """
        metadata = metadata or {}

        if self.strategy == ChunkStrategy.SEMANTIC:
            text_chunks = self._semantic_chunking(text)
        elif self.strategy == ChunkStrategy.SLIDING_WINDOW:
            text_chunks = self._sliding_window_chunking(text)
        else:
            text_chunks = self.splitter.split_text(text)

        chunks = []
        for idx, chunk_text in enumerate(text_chunks):
            chunk = Chunk(
                content=chunk_text,
                chunk_id=f"{document_id}_chunk_{idx}",
                document_id=document_id,
                chunk_index=idx,
                metadata={**metadata, "strategy": self.strategy.value},
                char_count=len(chunk_text)
            )
            chunks.append(chunk)

        return chunks

    def _semantic_chunking(self, text: str) -> List[str]:
        """
        Chunk by semantic boundaries (paragraphs with context).

        This strategy:
        1. Splits on paragraph boundaries
        2. Combines small paragraphs
        3. Ensures chunks don't exceed max size
        """
        # Split into paragraphs
        paragraphs = re.split(r'\n\s*\n', text)

        chunks = []
        current_chunk = []
        current_length = 0

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            para_length = len(para)

            # If paragraph alone exceeds chunk size, split it
            if para_length > self.chunk_size:
                # Save current chunk if exists
                if current_chunk:
                    chunks.append("\n\n".join(current_chunk))
                    current_chunk = []
                    current_length = 0

                # Split large paragraph
                sentences = re.split(r'(?<=[.!?])\s+', para)
                temp_chunk = []
                temp_length = 0

                for sentence in sentences:
                    sent_length = len(sentence)
                    if temp_length + sent_length > self.chunk_size:
                        if temp_chunk:
                            chunks.append(" ".join(temp_chunk))
                        temp_chunk = [sentence]
                        temp_length = sent_length
                    else:
                        temp_chunk.append(sentence)
                        temp_length += sent_length + 1

                if temp_chunk:
                    chunks.append(" ".join(temp_chunk))

            # If adding paragraph exceeds chunk size, save current chunk
            elif current_length + para_length > self.chunk_size:
                if current_chunk:
                    chunks.append("\n\n".join(current_chunk))
                current_chunk = [para]
                current_length = para_length

            # Otherwise, add to current chunk
            else:
                current_chunk.append(para)
                current_length += para_length + 2  # +2 for \n\n

        # Add remaining chunk
        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        return chunks

    def _sliding_window_chunking(self, text: str) -> List[str]:
        """
        Create overlapping chunks with sliding window.

        Useful for ensuring important content at chunk boundaries isn't lost.
        """
        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]

            # Try to end at sentence boundary
            if end < len(text):
                last_period = chunk.rfind('. ')
                if last_period > self.chunk_size // 2:
                    chunk = chunk[:last_period + 1]
                    end = start + last_period + 1

            chunks.append(chunk.strip())

            # Move start forward (with overlap)
            start = end - self.chunk_overlap

        return chunks

    def chunk_multiple_documents(
        self,
        documents: List[Dict[str, Any]]
    ) -> List[Chunk]:
        """
        Chunk multiple documents.

        Args:
            documents: List of dicts with 'id', 'text', and optional 'metadata'

        Returns:
            List of all chunks
        """
        all_chunks = []

        for doc in documents:
            chunks = self.chunk_document(
                text=doc['text'],
                document_id=doc['id'],
                metadata=doc.get('metadata', {})
            )
            all_chunks.extend(chunks)

        return all_chunks

    def get_chunk_statistics(self, chunks: List[Chunk]) -> Dict[str, Any]:
        """Get statistics about chunks."""
        if not chunks:
            return {}

        char_counts = [c.char_count for c in chunks]

        return {
            "total_chunks": len(chunks),
            "total_characters": sum(char_counts),
            "avg_chunk_size": sum(char_counts) / len(chunks),
            "min_chunk_size": min(char_counts),
            "max_chunk_size": max(char_counts),
            "unique_documents": len(set(c.document_id for c in chunks)),
            "strategy": self.strategy.value
        }


# Example usage
if __name__ == "__main__":
    # Sample document
    sample_doc = """
    Marketing Campaign Analysis Best Practices

    Effective marketing campaign analysis requires a systematic approach to data collection and interpretation.

    Data Collection
    First, ensure you're tracking the right metrics. Common KPIs include impression count, click-through rates (CTR), conversion rates, and return on ad spend (ROAS). Use tracking pixels and UTM parameters to accurately attribute conversions.

    Campaign Segmentation
    Break down your analysis by campaign type, channel, audience segment, and time period. This granular view helps identify what's working and what isn't. For example, email campaigns might perform better with certain demographics, while social media ads resonate with others.

    Performance Benchmarking
    Compare your results against industry benchmarks and historical data. A 2% CTR might seem low in isolation, but could be excellent for your industry. Track performance over time to identify trends and seasonality.

    Attribution Modeling
    Understand the customer journey. Did they convert after the first touchpoint or after multiple interactions? Multi-touch attribution helps allocate credit appropriately across channels.

    A/B Testing
    Never stop testing. Test subject lines, ad copy, images, calls-to-action, and landing pages. Use statistical significance testing to ensure your results are valid.

    Reporting and Insights
    Create actionable reports that tell a story. Don't just show numbers—explain what they mean and what actions should be taken. Use visualizations to make data accessible.

    Continuous Optimization
    Marketing is iterative. Use insights from each campaign to improve the next one. Build a knowledge base of what works for your audience.
    """

    print("=" * 80)
    print("Document Chunking Demonstrations")
    print("=" * 80)

    # Test different chunking strategies
    strategies = [
        (ChunkStrategy.RECURSIVE, "Recursive (smart boundaries)"),
        (ChunkStrategy.SEMANTIC, "Semantic (paragraph-based)"),
        (ChunkStrategy.SLIDING_WINDOW, "Sliding Window (overlapping)"),
        (ChunkStrategy.FIXED, "Fixed Size")
    ]

    for strategy, description in strategies:
        print(f"\n📄 Strategy: {description}")
        print("-" * 80)

        chunker = DocumentChunker(
            strategy=strategy,
            chunk_size=300,
            chunk_overlap=50
        )

        chunks = chunker.chunk_document(
            text=sample_doc,
            document_id="campaign_analysis_guide",
            metadata={"category": "marketing", "author": "Tech Hub"}
        )

        stats = chunker.get_chunk_statistics(chunks)

        print(f"Total chunks: {stats['total_chunks']}")
        print(f"Avg chunk size: {stats['avg_chunk_size']:.0f} chars")
        print(f"Size range: {stats['min_chunk_size']}-{stats['max_chunk_size']} chars")

        print(f"\nFirst chunk preview:")
        print(f"{chunks[0].content[:200]}...")

        print(f"\nChunk IDs: {[c.chunk_id for c in chunks]}")
