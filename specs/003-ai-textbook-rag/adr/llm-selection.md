# ADR-002: LLM for Textbook Generation

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-04
- **Feature:** AI-Native Textbook Generation with RAG Chatbot
- **Context:** The project requires an LLM to generate the core textbook content, including 6 chapters, suggested layout, diagrams (placeholders), and code snippets. The generated content must be structured, verifiable, and technically accurate.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The decision is to use a free-tier accessible LLM, such as GPT (e.g., GPT-3.5 or GPT-4 if free-tier usage allows) or Claude (e.g., Sonnet, Haiku if free-tier usage allows), for generating the textbook content in Markdown format.

## Consequences

### Positive

Flexible content generation, support for structured outputs (Markdown), ability to incorporate code snippets and diagram suggestions, and ease of integration with a RAG system for context awareness.

### Negative

Potential for free-tier rate limits, requiring careful management of API calls. Manual review of generated content may be needed to ensure technical accuracy and consistency, adding a human-in-the-loop step.

## Alternatives Considered

Dedicated content generation platforms/APIs: Offers specialized features for content creation but might not be free-tier compatible and could introduce vendor lock-in. Rejected due to cost and flexibility concerns.
Self-hosted open-source LLMs: Provides full control over the model and avoids API costs, but requires significant infrastructure and expertise to set up and maintain, making it unsuitable for a free-tier focused project. Rejected due to complexity and resource requirements.

## References

- Feature Spec: specs/003-ai-textbook-rag/spec.md
- Implementation Plan: specs/003-ai-textbook-rag/plan.md
- Related ADRs: ADR-001: Embedding Model Selection for RAG
- Evaluator Evidence: null