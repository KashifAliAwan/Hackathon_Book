# ADR-003: RAG Content Chunking Strategy

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-04
- **Feature:** AI-Native Textbook Generation with RAG Chatbot
- **Context:** The RAG chatbot relies on breaking down the textbook content into manageable chunks for embedding and retrieval. The chunking strategy directly impacts the relevance and accuracy of search results and overall system performance.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The decision is to chunk textbook content into segments of 300–500 tokens with a 50-token overlap between consecutive chunks.

## Consequences

### Positive

This strategy facilitates efficient RAG retrieval by providing sufficiently detailed context within each chunk while maintaining continuity across chunks due to the overlap. It is compatible with free-tier embedding models and generally leads to accurate answers and smooth chatbot navigation.

### Negative

Smaller chunk sizes can lead to a larger number of embeddings, potentially increasing storage and processing costs for the vector database (Qdrant). Conversely, larger chunks might reduce the precision of Q&A by including too much irrelevant context, or exceeding the context window of smaller LLMs.

## Alternatives Considered

Larger chunk sizes (e.g., 800+ tokens with no overlap): Simplifies embedding generation (fewer chunks) but risks including too much noise and reducing retrieval accuracy. Continuity between chunks would also be lost, potentially leading to disjointed answers. Rejected due to potential impact on answer quality and context loss.
Sentence-level or paragraph-level chunking: Offers highly granular context but significantly increases the number of embeddings, leading to higher costs and potentially slower retrieval due to more vector lookups. Rejected due to increased complexity and cost.

## References

- Feature Spec: specs/003-ai-textbook-rag/spec.md
- Implementation Plan: specs/003-ai-textbook-rag/plan.md
- Related ADRs: ADR-001: Embedding Model Selection for RAG, ADR-002: LLM for Textbook Generation
- Evaluator Evidence: null