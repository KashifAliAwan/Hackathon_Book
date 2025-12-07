# ADR-001: Embedding Model Selection for RAG

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-04
- **Feature:** AI-Native Textbook Generation with RAG Chatbot
- **Context:** The RAG chatbot functionality requires an embedding model to convert text into vector representations for similarity search. The project aims for free-tier compatibility and sufficient accuracy for textbook-based Q&A.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The decision is to use a free-tier compatible embedding model, such as OpenAI's `text-embedding-3-small` or an equivalent open-source model (e.g., `all-MiniLM-L6-v2` from Sentence Transformers).

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

Fast inference, free-tier cost, easy integration with existing RAG frameworks, sufficient accuracy for typical textbook Q&A.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

Potentially slightly less accurate than larger, more expensive embedding models, which might lead to less precise RAG retrieval in complex scenarios.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

Larger, paid embedding models (e.g., OpenAI's larger models, Cohere, etc.): Offer higher accuracy but incur significant costs, going against the free-tier compatibility goal. Rejected due to cost constraints.
Alternative Stack B: Self-hosting very large open-source models: Offers full control and potentially high accuracy, but requires significant computational resources and expertise, making it unsuitable for a free-tier focused project. Rejected due to complexity and resource requirements.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs/003-ai-textbook-rag/spec.md
- Implementation Plan: specs/003-ai-textbook-rag/plan.md
- Related ADRs: null
- Evaluator Evidence: null <!-- link to eval notes/PHR showing graders and outcomes -->