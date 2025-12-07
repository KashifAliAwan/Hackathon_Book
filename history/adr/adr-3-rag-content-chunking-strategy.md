# ADR-3: RAG Content Chunking Strategy

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-06
- **Feature:** 003-ai-textbook-rag
- **Context:** The effectiveness of the RAG chatbot heavily depends on how the textbook content is split into chunks for embedding and retrieval.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The chunking strategy will involve splitting the textbook content first by headings/sections, and then by tokens. Each chunk will be 800–1000 tokens long with a 100–150 token overlap.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

Improved RAG retrieval accuracy by preserving semantic context within sections; reduced noise and more relevant search results.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

Requires careful implementation of the chunking logic; incorrect chunking can still lead to irrelevant retrieval or fragmented context.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Fixed-size chunks without structural awareness:** Simpler to implement but can break semantically important sections, leading to lower retrieval quality.
- **Overlapping chunks only:** Provides some context preservation but doesn't leverage the inherent structure of the textbook, potentially creating less coherent chunks at section boundaries.
- **Larger or smaller chunk sizes:** Deviating significantly from the chosen token range might either dilute context (too small) or include too much irrelevant information (too large), negatively impacting embedding quality and retrieval speed.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs/003-ai-textbook-rag/spec.md
- Implementation Plan: specs/003-ai-textbook-rag/plan.md
- Related ADRs: adr-1-llm-for-textbook-generation.md, adr-2-embedding-model-for-rag.md
- Evaluator Evidence: