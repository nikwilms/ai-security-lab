# 1. Govern: scope and rules

*Why:* a test without a clear scope cannot be judged or repeated.

- **System purpose:** <what the AI system does, for whom>
- **Owner:** <for a sandbox: "lab sandbox, self">
- **Model sourcing:** [ ] provider API (ready-made model) [ ] self-hosted open weights [ ] own trained / fine-tuned
- **AI Act risk class (first view):** [ ] minimal [ ] limited [ ] high [ ] unacceptable — reason: <...>
- **Access level:** [ ] black box [ ] gray box [ ] white box — what I was given: <...>
- **In scope:** <components, interfaces, tools>
- **Out of scope:** <...>
- **Rules of engagement:**
  - Test only this target.
  - Synthetic data only.
  - Keep raw evidence in `evidence/` (not committed).
- **Learning goal:** <which exam topic / skill this project trains>
