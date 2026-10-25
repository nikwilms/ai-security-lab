# 4. Reduce: hypotheses and tests

*Why:* a written hypothesis keeps the test honest. Refuted hypotheses are results too.

Rules: one change per test · baseline · negative control · at least 5 trials, fresh session each.

## H1: <short name>

- **Written on:** <date, time — before the run>
- **Target and scope:** <component>
- **Invariant (must always hold):** <...>
- **Prediction if the weakness exists:** <...>
- **Observables:** <tool calls, output text, outbound requests>
- **Pass / fail rule:** <...>
- **Baseline:** <same task without the test input>
- **Negative control:** <harmless input that looks similar>
- **Tool:** promptfoo / garak / Inspect + AgentDojo / manual
- **Trials (k):** <n>
- **Result:** confirmed / refuted / inconclusive — <hits>/<k>

## Results file

Record every trial in `results.json` (format: `tools/passk/result_schema.json`).
Then run `make score P=<this project folder>`.
