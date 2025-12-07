# ADR-1: LLM for Textbook Generation

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-06
- **Feature:** 003-ai-textbook-rag
- **Context:** The project requires an AI-native textbook generation. A key decision is the choice of the Large Language Model (LLM) to generate the textbook content.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The Gemini model (via Claude Code Router) will be used as the main model for generating textbook content.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

High-quality, structured textbook content; streamlined integration.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

Potential cost implications if usage exceeds free-tier limits, dependency on Gemini API availability and performance.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Claude:** While Claude is available, Gemini is chosen for its potential strengths in long-form content generation and structured output, which aligns well with textbook creation.
- **OpenAI GPT Models:** Powerful models, but cost considerations and integration with the Claude Code Router favored Gemini.
- **Llama 2 (Open-source):** Offers flexibility and cost savings for local deployment, but may require more fine-tuning and computational resources to match the quality of proprietary models for complex textbook content.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs/003-ai-textbook-rag/spec.md
- Implementation Plan: specs/003-ai-textbook-rag/plan.md
- Related ADRs:
- Evaluator Evidence: