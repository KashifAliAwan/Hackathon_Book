---
description: "Task list for AI-Native Textbook Generation with RAG Chatbot"
---

# Tasks: AI-Native Textbook Generation with RAG Chatbot

**Input**: Design documents from `/specs/003-ai-textbook-rag/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are not explicitly requested in the feature specification for this initial task generation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths assume a project structure where `docusaurus.config.js`, `src/pages/`, `docs/` are at the root, and `rag_backend/` is a separate directory for the FastAPI application.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize Docusaurus v2 project in the root directory.
- [ ] T002 Configure Docusaurus `docusaurus.config.js` with site metadata, plugins, and theme settings.
- [ ] T003 Create `src/pages/index.js` for the Docusaurus landing page.
- [ ] T004 Create a `docs/` directory at the root for the generated textbook content.
- [ ] T005 Initialize `rag_backend` directory and Python environment for FastAPI.
- [ ] T006 Configure environment variables for LLM, Qdrant, and Neon connections.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Define initial Neon Serverless Postgres schema for `textbooks` and `chapters` tables in `rag_backend/database.py`.
- [ ] T008 Implement database connection and ORM setup in `rag_backend/database.py`.
- [ ] T009 Implement Qdrant client initialization and collection management in `rag_backend/qdrant_client.py`.
- [ ] T010 Implement embedding model loading and inference (Gemini text-embedding-004) in `rag_backend/embedding_model.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Generate Textbook Content (Priority: P1) 🎯 MVP

**Goal**: A complete, Markdown-formatted textbook with 6 chapters, suggested layout, diagrams, and code snippets can be generated and displayed.

**Independent Test**: A complete textbook with 6 chapters, suggested layout, diagrams, and code snippets can be generated and displayed.

### Implementation for User Story 1

- [ ] T011 [US1] Implement LLM client and content generation logic (using Gemini) in `rag_backend/textbook_generator.py`.
- [ ] T012 [US1] Implement iterative generation (outline-first, section by section) for textbook content in `rag_backend/textbook_generator.py`.
- [ ] T013 [US1] Integrate LLM for generating chapter outlines in `rag_backend/textbook_generator.py`.
- [ ] T014 [US1] Integrate LLM for generating detailed chapter content, including placeholders for diagrams and code snippets, in `rag_backend/textbook_generator.py`.
- [ ] T015 [US1] Implement logic to save generated Markdown content to `docs/` directory in `rag_backend/textbook_generator.py`.
- [ ] T016 [US1] Implement auto-generated sidebar functionality for Docusaurus in `docusaurus.config.js` and related Docusaurus files.
- [ ] T017 [US1] Create a FastAPI endpoint to trigger textbook generation in `rag_backend/main.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Interact with RAG Chatbot (Priority: P1)

**Goal**: The RAG chatbot can answer questions based on the textbook content, using free-tier compatible embeddings.

**Independent Test**: The RAG chatbot can answer questions based on the textbook content, using free-tier compatible embeddings.

### Implementation for User Story 2

- [ ] T018 [US2] Implement content chunking strategy (headings/sections, 800-1000 tokens, 100-150 overlap) in `rag_backend/chunking.py`.
- [ ] T019 [US2] Implement embedding generation and storage in Qdrant for textbook content in `rag_backend/rag_pipeline.py`.
- [ ] T020 [US2] Implement retrieval from Qdrant based on user queries in `rag_backend/rag_pipeline.py`.
- [ ] T021 [US2] Implement LLM integration for generating chatbot responses based on retrieved context in `rag_backend/rag_pipeline.py`.
- [ ] T022 [US2] Create a FastAPI endpoint for the RAG chatbot in `rag_backend/main.py`.
- [ ] T023 [US2] Design and implement the RAG chatbot UI/integration within Docusaurus `src/pages/index.js` or a new component.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Optional Urdu Translation (Priority: P2)

**Goal**: A generated chapter can be translated into Urdu.

**Independent Test**: A generated chapter can be translated into Urdu.

### Implementation for User Story 3

- [ ] T024 [US3] Implement LLM-based translation logic for Urdu in `rag_backend/translation.py`.
- [ ] T025 [US3] Integrate Urdu translation into the textbook generation service (optional parameter in `rag_backend/textbook_generator.py`).
- [ ] T026 [US3] Add UI elements in Docusaurus for selecting Urdu translation in `src/pages/index.js` or a dedicated settings component.

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Optional Personalized Chapters (Priority: P2)

**Goal**: A chapter can be personalized based on a user's specified interest.

**Independent Test**: A chapter can be personalized based on a user's specified interest.

### Implementation for User Story 4

- [ ] T027 [US4] Implement logic for integrating personalization preferences into LLM prompts in `rag_backend/textbook_generator.py`.
- [ ] T028 [US4] Add UI elements in Docusaurus for specifying personalization preferences in `src/pages/index.js` or a dedicated settings component.

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T029 Implement robust error handling and logging across FastAPI services.
- [ ] T030 Review and optimize performance of RAG chatbot and textbook generation.
- [ ] T031 Write a demo video script and record the demo (maximum 90 seconds).
- [ ] T032 Set up GitHub Actions for CI/CD pipeline to deploy Docusaurus to GitHub Pages/Vercel.
- [ ] T033 Ensure all secrets are managed using environment variables.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1 - Generate Textbook Content)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1 - Interact with RAG Chatbot)**: Can start after Foundational (Phase 2) - No direct dependency on US1 completion for core functionality, but benefits from US1 generated content.
- **User Story 3 (P2 - Optional Urdu Translation)**: Depends on User Story 1 generated content.
- **User Story 4 (P2 - Optional Personalized Chapters)**: Depends on User Story 1 generated content.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (none explicitly marked as such in this list, but can be if applicable).
- All Foundational tasks marked [P] can run in parallel (none explicitly marked as such in this list, but can be if applicable).
- Once Foundational phase completes, User Story 1 and User Story 2 can start in parallel.
- Tasks within each user story can be run in parallel if they operate on different files and have no dependencies.
- Different user stories (after foundational phase) can be worked on in parallel by different team members.

---

## Parallel Example: User Story 1 & 2 (after foundational phase)

```bash
# Developer A works on User Story 1:
Task: "Implement LLM client and content generation logic (using Gemini) in `rag_backend/textbook_generator.py`"
Task: "Implement iterative generation (outline-first, section by section) for textbook content in `rag_backend/textbook_generator.py`"
# ... and so on for US1 tasks

# Developer B works on User Story 2:
Task: "Implement content chunking strategy (headings/sections, 800-1000 tokens, 100-150 overlap) in `rag_backend/chunking.py`"
Task: "Implement embedding generation and storage in Qdrant for textbook content in `rag_backend/rag_pipeline.py`"
# ... and so on for US2 tasks
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
