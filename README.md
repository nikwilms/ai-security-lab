# AI Security Lab — project template

A template for small, structured AI security learning projects.
Every project follows the same frame, so each one teaches the method and ends as a short, readable report.

**Frame:** OWASP AI Exchange **G.U.A.R.D** (Govern, Understand, Adapt, Reduce, Demonstrate),
tested with the methods of the OWASP GenAI Red Teaming Manual, on the sandboxes of the
[GenAI Red Team Lab](https://github.com/GenAI-Security-Project/GenAI-Red-Team-Lab).

---

## How to use

1. On GitHub: **Use this template → Create a new repository** (or keep one repo and add projects inside it).
2. Open it in a **Codespace** (`Code → Codespaces → Create codespace`). Python, Node and Docker are ready.
3. Start a project:

   ```bash
   make new NAME=prompt-injection-llm-local
   ```

   This copies `projects/_template` to `projects/001-prompt-injection-llm-local/`.
4. Work through the files **in order** (01 → 05). Each file says what goes in and why.
5. Score your results:

   ```bash
   make score P=projects/001-prompt-injection-llm-local
   ```

6. Fill in the project card (`README.md` in the project folder) and commit.

> **Never commit secrets or raw evidence.** API keys go in `.env`. Raw logs go in `evidence/`. Both are in `.gitignore`.

---

## One project = five files

| Step | File | G.U.A.R.D | Question it answers |
|---|---|---|---|
| 1 | `01_govern_scope.md` | Govern | What exactly do I test, and what are the rules? |
| 2 | `02_understand_model.md` | Understand | How does the system work, and which threats apply? |
| 3 | `03_adapt_controls.md` | Adapt | Which protections are already there? |
| 4 | `04_reduce_tests/` | Reduce | Does the weakness exist? How often? How bad? |
| 5 | `05_demonstrate_report.md` | Demonstrate | What is the result, the evidence and the fix? |

Why this order: you learn what to look for before you look for it, and every finding ends with a fix.
See [`docs/method.md`](docs/method.md) for the full method and the rules.

---

## Repository structure

```text
.
├── .devcontainer/          Codespaces setup (Python, Node, Docker)
├── docs/
│   ├── method.md           G.U.A.R.D + test rules + scoring + severity
│   └── learning-path.md    project ideas mapped to EXIN AISP topics and sandboxes
├── projects/
│   └── _template/          copied for each new project
├── scripts/new_project.py  used by `make new`
├── tools/passk/            pass@k scoring (from the GenAI Red Team Lab, Apache-2.0)
└── Makefile
```

---

## Toolchain

| Purpose | Tool |
|---|---|
| Targets | GenAI Red Team Lab `sandboxes/` (llm_local, llm_remote, RAG_local, mcp_local, llm_memory_local) |
| Recon | GenAI Red Team Lab `exploitation/system_reconnaissance` |
| Automated tests | [promptfoo](https://www.promptfoo.dev/), [garak](https://github.com/NVIDIA/garak) |
| Agent benchmarks | [Inspect](https://inspect.aisi.org.uk/) + AgentDojo |
| Scoring | `tools/passk` |
| Learning lab | [OWASP PwnzzAI](https://github.com/OWASP/PwnzzAI) |
| Reference | [OWASP AI Exchange](https://owaspai.org/) |

---

## Credits

- Method: OWASP AI Exchange, OWASP GenAI Red Teaming Manual v1.0.
- `tools/passk/redteam_eval.py` and `result_schema.json`: copied unchanged from the
  [GenAI Red Team Lab](https://github.com/GenAI-Security-Project/GenAI-Red-Team-Lab)
  (`tutorials/evaluation_framework_passk`), licensed under Apache-2.0 (see `tools/passk/LICENSE-APACHE-2.0`).
