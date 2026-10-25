# 5. Demonstrate: report

*Why:* a result only counts if someone else can understand and repeat it.

## Summary (3–5 sentences, for a non-technical reader)

<What was tested. What broke. The biggest risk. The top fixes.>

## Findings

| ID | Finding | AI Exchange | LLM / ASI / ATLAS | k | Hits | Rate (95 % CI) | Outcome | Severity | Recommended control |
|---|---|---|---|---|---|---|---|---|---|
| F-001 | | | | | | | | | |

Copy rate, interval and outcome from `04_reduce_tests/report.md` (made by `make score`).
Severity scale: see `docs/method.md`.

## Evidence (kept private in `evidence/`)

- Model, version, endpoint, date
- Settings: temperature, seed, max tokens
- Raw logs / transcripts, with SHA-256 hashes

## Coverage

- Tested: <threats>
- Not tested: <threats and why>
- Inconclusive: <threats>

## Regression and retest

- Regression tests: <where, how to rerun>
- Retest after fix: <date, result>

## Limits

<sample size, sandbox vs. real system, model version drift, ...>
