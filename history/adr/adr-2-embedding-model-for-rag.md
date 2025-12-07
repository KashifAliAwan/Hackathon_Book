# ADR-2: Embedding Model for RAG

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-06
- **Feature:** 003-ai-textbook-rag
- **Context:** The RAG chatbot requires an embedding model to convert textbook content into vector representations for efficient similarity search.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The Gemini embedding model (text-embedding-004) will be used as the embedding model for the RAG chatbot.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

High-quality embeddings, good integration with other Gemini services (if used), potentially optimized for performance.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

Potential cost implications if usage exceeds free-tier limits, dependency on Gemini API availability and performance.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **OpenAI Embeddings (text-embedding-ada-002):** A strong alternative with good performance, but cost considerations and integration with Gemini-centric architecture favored Gemini's model.
- **Sentence Transformers (e.g., `all-MiniLM-L6-v2`):** Open-source and free-tier compatible, offering local deployment options. Rejected for potentially lower quality compared to proprietary models for complex technical content and the preference for a single vendor solution (Gemini) for both LLM and embeddings.
- **Hugging Face Inference API:** Offers a wide range of models but has usage limits and potential latency issues depending on the chosen model and tier.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs/003-ai-textbook-rag/spec.md
- Implementation Plan: specs/003-ai-textbook-rag/plan.md
- Related ADRs: adr-1-llm-for-textbook-generation.md
- Evaluator Evidence: