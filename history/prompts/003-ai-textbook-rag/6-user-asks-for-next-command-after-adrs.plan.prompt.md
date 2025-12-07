---
id: 6
title: User Asks for Next Command After ADRs
stage: plan
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: 003-ai-textbook-rag
branch: 003-ai-textbook-rag
user: user
command: what should next command?
labels: [planning, workflow]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
tests:
---

## Prompt

what should next command?

## Response snapshot

The next command should be `/sp.tasks` to generate the implementation tasks.

## Outcome

- ✅ Impact: Provided the next command in the Spec-Driven Development workflow.
- 🧪 Tests: null
- 📁 Files: history/prompts/003-ai-textbook-rag/6-user-asks-for-next-command-after-adrs.plan.prompt.md
- 🔁 Next prompts: Generate implementation tasks using /sp.tasks.
- 🧠 Reflection: Successfully guided the user to the next step of the workflow.

## Evaluation notes (flywheel)

- Failure modes observed: User interrupted tool use for PHR creation.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
