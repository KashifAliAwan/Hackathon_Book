<!--
Sync Impact Report:
Version change: 0.0.0 -> 1.0.0 (MINOR: Initial constitution defined)
Modified principles:
  - [PROJECT_NAME] -> 1. Project Goal (Global Objective)
  - [PRINCIPLE_1_NAME] -> 2. Quality & Delivery Standards (Global Rules)
  - [PRINCIPLE_2_NAME] -> 3. MCP & Documentation Compliance
  - [PRINCIPLE_3_NAME] -> 4. Mandatory Deliverables (Required for Completion)
  - [PRINCIPLE_4_NAME] -> 5. Non-Negotiable Rules
  - [PRINCIPLE_5_NAME] -> 6. Bonus Scoring Constraints
Added sections: None (existing template sections filled)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/commands/sp.constitution.md: ✅ updated
  - .specify/templates/commands/sp.phr.md: ⚠ pending
  - .specify/templates/commands/sp.specify.md: ⚠ pending
  - .specify/templates/commands/sp.plan.md: ⚠ pending
  - .specify/templates/commands/sp.tasks.md: ⚠ pending
  - .specify/templates/commands/sp.git.commit_pr.md: ⚠ pending
  - .specify/templates/commands/sp.clarify.md: ⚠ pending
  - .specify/templates/commands/sp.checklist.md: ⚠ pending
  - .specify/templates/commands/sp.analyze.md: ⚠ pending
  - .specify/templates/commands/sp.adr.md: ⚠ pending
  - .specify/templates/commands/sp.implement.md: ⚠ pending
Follow-up TODOs:
  - TODO(RATIFICATION_DATE): Original adoption date unknown.
-->
# Physical AI & Humanoid Robotics (AI-Native Textbook) Constitution

## Core Principles

### 1. Project Goal (Global Objective)
- Create a complete **AI-native textbook** on *Physical AI & Humanoid Robotics*.
- The book must include:
  - Intelligent agents
  - Integrated chatbot
  - Public deployment (web)

### 2. Quality & Delivery Standards (Global Rules)
These rules apply to **all work** in this project:
- The book **must be built using Docusaurus**
- The book **must be deployed** on GitHub Pages or Vercel
- All source code and content **must be in a public GitHub repository**
- All AI-generated content must be:
  - Structured
  - Verifiable
  - Technically accurate
- Every technical claim **must be logically justified**
- All chapters must follow a **consistent format**
- Primary language: **English**
- Clarity is mandatory: students must easily understand the content

### 3. MCP & Documentation Compliance
- **Context7 MCP must be connected and used**
- Official **Docusaurus documentation must be referenced via MCP**
- All Docusaurus configuration, structure, and plugins must follow
  the **latest official Docusaurus docs pulled through MCP**
- No guesswork allowed for configuration — documentation must be verified

### 4. Mandatory Deliverables (Required for Completion)
The project is considered incomplete without:
- ✅ AI-driven textbook
- ✅ Integrated RAG chatbot
- ✅ Public GitHub repository
- ✅ Demo video (maximum 90 seconds)
- ✅ Live deployed website
- ✅ Usage of Claude Code and Spec-Kit Plus

### 5. Non-Negotiable Rules
These rules cannot be violated:
- **Zero plagiarism** (strictly enforced)
- Content must be **original and project-specific**
- Git history must remain **clean and readable**
- Constitution must be **committed before running `/sp.specify`**
- Full Spec-Kit Plus workflow must be followed

### 6. Bonus Scoring Constraints
The following features provide extra points:
- Use of Claude Code **Subagents**
- Signup / Signin system
- Urdu translation support
- Personalized learning features

## Additional Constraints

All changes must be small, testable, and reference code precisely.
All AI-generated content must be structured, verifiable, and technically accurate.

## Development Workflow

The full Spec-Kit Plus workflow must be followed. TDD (Test-Driven Development) is mandatory: tests are written, user approved, tests fail, then implementation. Red-Green-Refactor cycle strictly enforced.

## Governance
This constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date unknown. | **Last Amended**: 2025-12-04
