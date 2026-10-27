# AI Security Lab practice notes

Hands-on practice for AI security and AI red teaming: one folder per lab, one note per exercise.
Learning track for the EXIN AI Security Professional (OWASP AI Exchange).

Larger, finished work lives in its own repositories:
- [agent-evals](https://github.com/nikwilms/agent-evals) â€” prompt-injection evaluations of LLM agents

## Labs

| Lab | Topic | Notes |
|---|---|---|
| [OWASP PwnzzAI](https://github.com/OWASP/PwnzzAI) | Prompt injection, levels 1â€“3 | [labs/pwnzzai/prompt-injection-levels-1-3.md](labs/pwnzzai/prompt-injection-levels-1-3.md) |

## How each note is written

Every note follows [`labs/_note-template.md`](labs/_note-template.md):
test setup â†’ hypothesis per experiment â†’ result â†’ OWASP AI Exchange mapping â†’ mitigations â†’ takeaway.

## Rules

- No secrets, API keys or raw logs in this repo.
- No full solutions for labs that ask not to publish them (e.g. DVAA). Notes describe the method and the lesson, not the answer.
- Lab environments run in GitHub Codespaces, not on the local machine.
