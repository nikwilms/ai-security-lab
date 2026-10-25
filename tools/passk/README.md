# pass@k scoring

`redteam_eval.py` and `result_schema.json` are copied unchanged from the
[GenAI Red Team Lab](https://github.com/GenAI-Security-Project/GenAI-Red-Team-Lab),
folder `tutorials/evaluation_framework_passk`, licensed under Apache-2.0 (see `LICENSE-APACHE-2.0`).
The full explanation of the method is in that tutorial's README.

Use from the repo root:

    make score P=projects/<folder>

It reads `04_reduce_tests/results.json` and writes `report.json` and `report.md` next to it.
