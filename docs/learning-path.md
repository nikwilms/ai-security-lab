# Learning path: small projects

Each project is small (1–3 sessions) and maps to an EXIN AI Security Professional (AISP) exam topic
and an OWASP AI Exchange section. Order: breadth first, then depth.

| # | Project | Target | AI Exchange | EXIN topic | LLM / ASI |
|---|---|---|---|---|---|
| 001 | Direct prompt injection on a plain chatbot | `llm_local` or `llm_remote` | 2.2.1 | 2.1 Input threats | LLM01 |
| 002 | System prompt and hidden context exposure | `llm_local` | 2.3.1, 4.6 | 2.1, 2.3 | LLM08 |
| 003 | Indirect prompt injection through documents | `RAG_local` | 2.2.2 | 2.1 | LLM01, ASI01 |
| 004 | Tool misuse on an agent with tools | `mcp_local` | 2.2.2, 4.8 | 1.2 Agentic risks | ASI01, ASI02 |
| 005 | Memory poisoning across sessions | `llm_memory_local` | 4.7 | 2.3 Runtime threats | ASI06 |
| 006 | Resource exhaustion and rate limits | `llm_remote` | 2.5 | 2.1 | LLM06 |
| 007 | Defense test: a guardrail in front of the model | any of the above + a filter | controls ch. 1 | 3.3 Limiting unwanted behavior | – |
| 008 | Threat model of a ready-made model deployment (no testing) | paper exercise | ch. 0 risk analysis | 1.2 Threat modeling, 3.1 Governance | – |
| 009 | Privacy review of a RAG system | `RAG_local` | ch. 6 | 5.1 Privacy | LLM02 |

Ideas for later: supply-chain checks of model files, multi-agent message tampering, a full AgentDojo
benchmark run with your own attack variants.

## Per project

1. `make new NAME=<short-name>`
2. Fill `01` to `05` in order.
3. Score with `make score P=projects/<folder>`.
4. Update the project card and the table above (status column optional).
