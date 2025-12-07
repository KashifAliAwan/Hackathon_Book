### Development Plan

---

### 1. Scope and Dependencies

**In Scope:**
*   Generation of a complete AI-native textbook in Markdown format with 6 chapters, including suggested layout, placeholders for diagrams, and code snippets.
*   Deployment of the textbook using Docusaurus v2 with an auto-generated sidebar.
*   Integration of a RAG chatbot backend using Qdrant (vector search), Neon Serverless Postgres (data storage), and FastAPI (API).
*   Utilization of free-tier compatible embeddings for the RAG chatbot.
*   Public GitHub repository for all source code and content.
*   Public deployment of the textbook (GitHub Pages or Vercel).
*   Demo video (maximum 90 seconds).
*   Usage of Claude Code and Spec-Kit Plus workflow.

**Out of Scope:**
*   Manual creation or editing of textbook content (content generation is AI-driven).
*   Complex authentication/authorization systems beyond basic free-tier capabilities (unless specified as a bonus).
*   Advanced NLP features for the chatbot beyond RAG functionality.
*   Real-time content updates or dynamic content generation on the deployed site (initial content is static, generated beforehand).
*   Custom Docusaurus plugins not directly related to textbook content or RAG integration.

**External Dependencies:**
*   **Docusaurus v2:** Framework for building the static textbook website. (Owned by Facebook Open Source).
*   **Qdrant:** Vector database for efficient similarity search in the RAG system. (Owned by Qdrant).
*   **Neon Serverless Postgres:** Scalable relational database for storing textbook metadata and potentially chat history. (Owned by Neon).
*   **FastAPI:** Python web framework for building the RAG chatbot API. (Owned by FastAPI community).
*   **Embedding Model:** A free-tier compatible embedding model (e.g., Sentence Transformers, OpenAI's `text-embedding-ada-002` if within free tier, or open-source alternatives like `all-MiniLM-L6-v2`). (Ownership depends on chosen model).
*   **Large Language Model (LLM):** For generating textbook content and chatbot responses. (e.g., Claude, OpenAI GPT models, Llama 2). (Ownership depends on chosen model).
*   **GitHub/Vercel:** Hosting and deployment platforms. (Owned by GitHub/Vercel).
*   **Claude Code & Spec-Kit Plus:** For development workflow and prompt history. (Owned by Anthropic).

---

### 2. Key Decisions and Rationale

**Decision 1: Docusaurus v2 as the Static Site Generator**
*   **Options Considered:** Next.js, Gatsby, MkDocs.
*   **Trade-offs:** Docusaurus is specifically designed for documentation sites, offering built-in features like versioning, search, and easy content management with Markdown/MDX. Next.js/Gatsby are more general-purpose React frameworks, requiring more setup for documentation features. MkDocs is simpler but less flexible for advanced features and React components.
*   **Rationale:** Aligns with the \"AI-native textbook\" goal, providing a robust, feature-rich, and easily maintainable platform for documentation. Explicitly mandated by the Constitution.
*   **Principles:** Smallest viable change (leverages existing, specialized tooling).

**Decision 2: RAG Stack - Qdrant, Neon Serverless Postgres, FastAPI**
*   **Options Considered:** Elasticsearch/OpenSearch, ChromaDB, Pinecone for vector DB; traditional Postgres, MongoDB for data storage; Flask, Node.js for API.
*   **Trade-offs:** Qdrant offers efficient vector search and good scalability. Neon Serverless Postgres provides a cost-effective, scalable relational database suitable for metadata and potentially chat history. FastAPI is a modern, high-performance Python web framework, ideal for building robust APIs quickly. Other options either lack specific features, are less cost-effective for free-tier, or have steeper learning curves for this specific stack.
*   **Rationale:** This combination provides a scalable, cost-effective (free-tier compatible), and performant RAG backend. Explicitly mandated by the Specification.
*   **Principles:** Measurable performance (FastAPI), smallest viable change (leveraging specialized tools), cost-effectiveness.

**Decision 3: Free-tier compatible embeddings**
*   **Options Considered:** OpenAI Embeddings (if free tier available), Sentence Transformers (e.g., `all-MiniLM-L6-v2`), Hugging Face Inference API.
*   **Trade-offs:** OpenAI offers high-quality embeddings but might incur costs beyond free-tier limits. Sentence Transformers are performant and can be run locally or on a small server, making them free-tier friendly. Hugging Face Inference API offers a wide range of models but also has usage limits.
*   **Rationale:** Adheres to the \"free-tier compatible embeddings\" requirement. `all-MiniLM-L6-v2` is a good balance of performance and efficiency for a free-tier solution.
*   **Principles:** Cost-effectiveness, measurable performance.

**Decision 4: AI Content Generation Strategy**
*   **Options Considered:** Single LLM call for entire chapter, iterative generation (section by section), outline-first generation.
*   **Trade-offs:** Single call is simpler but less controllable and prone to hallucinations for long content. Iterative generation provides more control and allows for better fact-checking/refinement. Outline-first helps structure.
*   **Rationale:** An outline-first, iterative generation approach combined with validation against technical accuracy ensures structured, verifiable, and accurate content as per the Constitution. This involves generating an outline, then generating content for each section based on the outline, and then refining.
*   **Principles:** Verifiable, technically accurate, structured content.


---

### 3. Interfaces and API Contracts

**A. Textbook Content Generation Service (Internal API)**
*   **Purpose:** To generate and structure textbook content based on prompts.
*   **Input:**
    *   `topic: str` (e.g., \"Physical AI & Humanoid Robotics\")
    *   `chapter_count: int` (e.g., 6)
    *   `chapter_outline_template: Optional[str]` (e.g., desired section headings)
    *   `language: Optional[str]` (e.g., \"English\", \"Urdu\")
    *   `personalization_preferences: Optional[Dict]` (e.g., \"focus_on\": \"reinforcement learning\")
*   **Output:**
    *   `textbook_content: List[Dict]`
        *   `chapter_title: str`
        *   `chapter_slug: str`
        *   `markdown_content: str` (full Markdown with placeholders)
        *   `diagram_suggestions: List[str]` (textual descriptions for diagrams)
        *   `code_snippet_suggestions: List[Dict]` (code descriptions with language hints)
*   **Errors:**
    *   `400 Bad Request`: Invalid input parameters.
    *   `500 Internal Server Error`: LLM generation failure, structuring errors.
*   **Versioning Strategy:** API versioning via URL (e.g., `/api/v1/generate_textbook`).
*   **Idempotency:** Generation requests can be idempotent if a unique request ID is provided, allowing re-requests without generating new content if the original is processing or completed.\n*   **Timeouts/Retries:** Client-side timeouts for long generation tasks (e.g., 5-10 minutes). Retries for transient network errors.

**B. RAG Chatbot API (FastAPI)**
*   **Purpose:** To answer user questions based on the textbook content.
*   **Endpoint:** `/api/v1/chat`
*   **Input:**
    *   `query: str` (user's question)
    *   `chat_history: Optional[List[Dict]]` (previous turns, if stateful)
    *   `textbook_id: str` (ID of the specific textbook being queried)
    *   `language: Optional[str]` (for multi-language support)
*   **Output:**
    *   `answer: str` (chatbot's response)
    *   `sources: List[Dict]` (references from the textbook)
        *   `chapter: str`
        *   `section: str`
        *   `page_link: str` (Docusaurus link)
*   **Errors:**
    *   `400 Bad Request`: Missing `query` or `textbook_id`.
    *   `404 Not Found`: `textbook_id` does not exist.
    *   `500 Internal Server Error`: Vector DB error, LLM response generation failure.
    *   `503 Service Unavailable`: Qdrant/Neon unavailable.
*   **Versioning Strategy:** API versioning via URL (e.g., `/api/v1/chat`).
*   **Idempotency:** Chat queries are generally not idempotent, but `textbook_id` ensures context consistency.
*   **Timeouts/Retries:** Client-side timeouts for chat responses (e.g., 30-60 seconds). Retries for transient network errors.

---

### 4. Non-Functional Requirements (NFRs) and Budgets

**A. Performance:**
*   **Textbook Generation Latency (SC-001):** Complete textbook generation (6 chapters) within 5 minutes.
    *   **Budget:** LLM API calls, embedding generation, Qdrant indexing, Markdown file writes.
    *   **Mitigation:** Asynchronous processing, parallel chapter generation (if LLM allows), optimized embedding/indexing.
*   **RAG Chatbot p95 Latency (SC-003):** Chatbot response within 5 seconds for 95% of requests.
    *   **Budget:** Vector search (Qdrant), RAG context retrieval, LLM inference.
    *   **Mitigation:** Efficient Qdrant indexing, optimized RAG pipeline, fast LLM inference (choose appropriate LLM).
*   **Throughput:** RAG chatbot supporting 10 concurrent users (initial free-tier target).
    *   **Budget:** FastAPI worker processes, Qdrant/Neon connection limits.
    *   **Mitigation:** FastAPI with Uvicorn, horizontal scaling for FastAPI (if needed).

**B. Reliability:**
*   **Uptime SLO:** Docusaurus site 99.9% uptime (handled by GitHub Pages/Vercel). RAG Chatbot API 99% uptime.
*   **Error Budget:** Max 1% error rate for RAG Chatbot API (SC-002: 90% accuracy implies 10% acceptable errors for irrelevance, but API errors should be lower).
*   **Degradation Strategy:** If RAG API fails, chatbot can return a generic \"I'm sorry, I cannot answer right now\" message.

**C. Security:**
*   **AuthN/AuthZ:** No user authentication for basic textbook viewing or RAG chatbot interaction in free-tier (unless bonus signup/signin is implemented). If implemented, use industry-standard OAuth2/JWT.\n*   **Data Handling:** Textbook content (generated Markdown) is public. User queries for RAG chatbot should not contain sensitive PII.\n*   **Secrets:** API keys for LLMs, Qdrant, Neon, etc., must be stored securely (e.g., environment variables, secret management services). Never hardcode.\n*   **Auditing:** Basic logging of RAG chatbot queries and responses for debugging and improvement.\n
**D. Cost:**
*   **Unit Economics:** Aim for free-tier compatibility for Qdrant, Neon, and embedding models. Monitor LLM token usage closely.\n*   **Budget:** Stay within free-tier limits for all services. Scale services only when required and with user consent.\n
---

### 5. Data Management and Migration

**A. Source of Truth:**
*   **Textbook Content:** Markdown files generated by the AI agent and stored in the Docusaurus `docs/` directory. These files will be version-controlled in Git.
*   **RAG Embeddings:** Stored in Qdrant. The source text for embeddings will be the processed Markdown content of the textbook.
*   **Textbook Metadata:** (e.g., chapter titles, slugs, last generated date, associated RAG index ID) stored in Neon Serverless Postgres.

**B. Schema Evolution (Neon Serverless Postgres):**
*   **Initial Schema:**

```sql
    CREATE TABLE textbooks (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        title VARCHAR(255) NOT NULL,
        language VARCHAR(50) NOT NULL DEFAULT 'english',
        version VARCHAR(50) NOT NULL,
        qdrant_collection_name VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE chapters (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        textbook_id UUID NOT NULL REFERENCES textbooks(id) ON DELETE CASCADE,
        chapter_number INT NOT NULL,
        title VARCHAR(255) NOTALL,
        slug VARCHAR(255) NOT NULL,
        file_path VARCHAR(500) UNIQUE NOT NULL,
        content_hash VARCHAR(64) NOT NULL, -- To detect content changes
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(textbook_id, chapter_number),
        UNIQUE(textbook_id, slug)
    );
    ```

*   **Evolution:** Use Alembic or similar database migration tools for schema changes. Each change should be backward-compatible if possible, or include a clear migration path.

**C. Migration and Rollback:**
*   **Textbook Content:** Handled by Git (version control of Markdown files).
*   **Qdrant Data:** Re-indexing Qdrant collections is the primary migration strategy for embedding changes or content updates.
*   **Neon Data:** Database migrations managed through scripts. Rollback involves applying previous migration scripts.

**D. Data Retention:**
*   Textbook Markdown files: Retained indefinitely in Git.
*   Qdrant embeddings: Retained as long as the associated textbook version is active. Old versions can be pruned.
*   Neon data: Retained indefinitely for active textbooks. Chat history might have a shorter retention policy (e.g., 30-90 days) depending on privacy and storage costs.

---

### 6. Operational Readiness

**A. Observability:**
*   **Logs:** Standard application logging (FastAPI, Docusaurus build process) to stdout/stderr. Structured logging (JSON) for easier parsing. Log levels (DEBUG, INFO, WARN, ERROR).
*   **Metrics:**
    *   **FastAPI:** Request latency, error rates, throughput for RAG API (e.g., using Prometheus/Grafana or similar).
    *   **Qdrant:** Vector search latency, collection size, indexing rates.
    *   **Neon:** Connection pool usage, query latency.
    *   **LLM Usage:** Token counts, API call costs.
*   **Traces:** Distributed tracing (e.g., OpenTelemetry) for RAG chatbot API calls to understand bottlenecks across components (FastAPI -> Qdrant -> LLM).

**B. Alerting:**
*   **Thresholds:**
    *   RAG API error rate > 5% for 5 minutes.
    *   RAG API p99 latency > 10 seconds for 5 minutes.
    *   Qdrant/Neon service unavailability.
    *   LLM API errors/rate limits.
*   **On-call Owners:** Initial project owner/developer.

**C. Runbooks for Common Tasks:**
*   \"How to deploy a new textbook version.\"\n*   \"How to re-index Qdrant collection.\"\n*   \"How to troubleshoot RAG chatbot errors.\"\n*   \"How to update Docusaurus dependencies.\"\n
**D. Deployment and Rollback strategies:**
*   **Textbook Content (Docusaurus):**
    *   Deployment: GitHub Actions to build Docusaurus site and deploy to GitHub Pages/Vercel on `main` branch merge.
    *   Rollback: Revert problematic Git commit and re-deploy.
*   **RAG Backend (FastAPI, Qdrant, Neon):**
    *   Deployment: Containerized deployment (e.g., Docker, Kubernetes). CI/CD pipeline (GitHub Actions) to build images and deploy to a cloud service (e.g., Google Cloud Run, AWS Fargate, Heroku).
    *   Rollback: Deploy previous stable Docker image version.

**E. Feature Flags and Compatibility:**
*   **Optional Features:** Urdu translation and personalized chapters can be controlled by feature flags in the RAG API or Docusaurus config.
*   **Compatibility:** Ensure API changes are backward-compatible. If not, communicate breaking changes clearly and provide migration guides.

---

### 7. Risk Analysis and Mitigation

**A. Risk 1: LLM Hallucinations and Technical Inaccuracies in Textbook Content.**
*   **Blast Radius:** Generated textbook contains incorrect or misleading information, impacting student learning and project credibility.
*   **Mitigation:**
    *   Iterative generation with human-in-the-loop review (initial drafts).
    *   Pre-defined structure and validation rules for AI-generated content.
    *   Prompt engineering techniques to emphasize accuracy, verification, and citing sources (even if AI-internal).
    *   Integration of fact-checking mechanisms (e.g., cross-referencing with trusted sources during generation, if possible within LLM context limits).
    *   Clear disclaimers on AI-generated content.
\n**B. Risk 2: High Costs for LLM and Embedding Services Beyond Free-Tier.**
*   **Blast Radius:** Project becomes financially unsustainable, blocking further development or deployment.
*   **Mitigation:**
    *   Strict monitoring of API usage and costs (LLM token counts, embedding service calls).
    *   Prioritize free-tier compatible open-source embedding models.
    *   Optimize RAG retrieval to minimize LLM calls (e.g., aggressive caching of embeddings, pre-calculating embeddings).
    *   Implement rate limiting and usage quotas for chatbot.
    *   Explore cheaper LLM alternatives or local LLM deployment for certain tasks (if feasible).

**C. Risk 3: RAG Chatbot Performance (Latency, Relevance, Scalability).**
*   **Blast Radius:** Chatbot is slow, provides irrelevant answers, or fails under moderate load, degrading user experience.\n*   **Mitigation:**
    *   Optimize Qdrant indexing parameters and hardware (if not serverless).
    *   Fine-tune chunking strategy for RAG (textbook content splitting).
    *   Experiment with different embedding models and RAG retrieval algorithms.
    *   Implement caching for frequent queries.
    *   Horizontal scaling for FastAPI application.
    *   Robust error handling and fallback responses for the chatbot.

---

### 8. Evaluation and Validation

**A. Definition of Done:**
*   All user stories (P1 and P2) implemented and acceptance scenarios passed.
*   Textbook generated according to FR-001/002 and rendered successfully in Docusaurus (FR-003, SC-004).
*   RAG chatbot fully integrated and operational (FR-004/005, SC-002/003).
*   Public GitHub repository established with clean Git history.
*   Live deployed website accessible.
*   Demo video created.
*   Full Spec-Kit Plus workflow followed, including PHRs and ADR suggestions.
*   Code adheres to Constitution's quality and delivery standards (e.g., zero plagiarism, consistent format).

**B. Output Validation:**
*   **Textbook Content:**
    *   Format: Validate generated Markdown structure (headings, lists, code blocks, image placeholders).
    *   Requirements: Verify presence of 6 chapters, suggested layout, diagram/code snippet placeholders.
    *   Safety/Accuracy: Manual review for technical accuracy and absence of harmful content (initial phases).
*   **RAG Chatbot Responses:**
    *   Relevance: Evaluate SC-002 (90% accuracy) through a test suite of questions and expected answers.
    *   Format: Ensure responses are coherent and cite sources correctly.
    *   Safety: Filter harmful responses from LLM.
*   **Docusaurus Deployment:** Verify site accessibility, correct rendering of content, and auto-generated sidebar functionality.

---

### 9. Architectural Decisions Documented

*   [ADR-1: LLM for Textbook Generation](history/adr/adr-1-llm-for-textbook-generation.md)
*   [ADR-2: Embedding Model for RAG](history/adr/adr-2-embedding-model-for-rag.md)
*   [ADR-3: RAG Content Chunking Strategy](history/adr/adr-3-rag-content-chunking-strategy.md)


---

### Critical Files for Implementation
*   `D:\\Programming Things\\GIAIC-Pakistan Zindabad\\Hackathon_Book\\docusaurus.config.js` - Core Docusaurus configuration for site metadata, plugins, and theme settings.\n*   `D:\\Programming Things\\GIAIC-Pakistan Zindabad\\Hackathon_Book\\src\\pages\\index.js` - The main entry point for the Docusaurus landing page, where the textbook generation trigger or RAG chatbot interface might reside.\n*   `D:\\Programming Things\\GIAIC-Pakistan Zindabad\\Hackathon_Book\\docs\\README.md` (or similar) - Placeholder for the generated textbook content. This will be the target directory for Markdown files.\n*   `D:\\Programming Things\\GIAIC-Pakistan Zindabad\\Hackathon_Book\\rag_backend\\main.py` (proposed) - The main FastAPI application file for the RAG chatbot.\n*   `D:\\Programming Things\\GIAIC-Pakistan Zindabad\\Hackathon_Book\\rag_backend\\database.py` (proposed) - Module for Neon Serverless Postgres connection and schema.
