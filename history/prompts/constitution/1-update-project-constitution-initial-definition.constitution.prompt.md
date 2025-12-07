---
id: 1
title: Update project constitution with initial definition
stage: constitution
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: unknown
command: /sp.constitution
labels: ["constitution", "initial setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - ./.specify/memory/constitution.md
tests: null
---

## Prompt

```text
# Constitution — Project-Wide Quality Standards
**Project:** Physical AI & Humanoid Robotics (AI-Native Textbook)

---

## 1. Project Goal (Global Objective)

- Create a complete **AI-native textbook** on *Physical AI & Humanoid Robotics*.
- The book must include:
  - Intelligent agents
  - Integrated chatbot
  - Public deployment (web)

---

## 2. Quality & Delivery Standards (Global Rules)

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

---

## 3. MCP & Documentation Compliance

- **Context7 MCP must be connected and used**
- Official **Docusaurus documentation must be referenced via MCP**
- All Docusaurus configuration, structure, and plugins must follow
  the **latest official Docusaurus docs pulled through MCP**
- No guesswork allowed for configuration — documentation must be verified

---

## 4. Mandatory Deliverables (Required for Completion)

The project is considered incomplete without:

- ✅ AI-driven textbook
- ✅ Integrated RAG chatbot
- ✅ Public GitHub repository
- ✅ Demo video (maximum 90 seconds)
- ✅ Live deployed website
- ✅ Usage of Claude Code and Spec-Kit Plus

---

## 5. Non-Negotiable Rules

These rules cannot be violated:

- **Zero plagiarism** (strictly enforced)
- Content must be **original and project-specific**
- Git history must remain **clean and readable**
- Constitution must be **committed before running `/sp.specify`**
- Full Spec-Kit Plus workflow must be followed

---

## 6. Bonus Scoring Constraints

The following features provide extra points:

- Use of Claude Code **Subagents**
- Signup / Signin system
- Urdu translation support
- Personalized learning features

---
```

## Response snapshot

The project constitution file `.specify/memory/constitution.md` was updated with the provided content. The constitution is now version 1.0.0. Several template files require review for consistency.

## Outcome

- ✅ Impact: Constitution updated and initial version established.
- 🧪 Tests: N/A
- 📁 Files: One file modified.
- 🔁 Next prompts: Review and update dependent templates.
- 🧠 Reflection: PHR creation script not found, used agent-native method.

## Evaluation notes (flywheel)

- Failure modes observed: PHR creation script missing.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure PHR script is available or improve agent-native PHR creation.
