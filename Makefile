.PHONY: new score test help

help:
	@echo "make new NAME=<short-name>     create a new project from the template"
	@echo "make score P=projects/<folder>  score 04_reduce_tests/results.json"
	@echo "make test                      run the scoring tool tests"

new:
	@test -n "$(NAME)" || (echo "Usage: make new NAME=<short-name>"; exit 1)
	python3 scripts/new_project.py $(NAME)

score:
	@test -n "$(P)" || (echo "Usage: make score P=projects/<folder>"; exit 1)
	python3 tools/passk/redteam_eval.py score $(P)/04_reduce_tests/results.json \
		--out-json $(P)/04_reduce_tests/report.json --out-md $(P)/04_reduce_tests/report.md

test:
	python3 -c "import json; json.load(open(\"projects/_template/04_reduce_tests/results.json\"))" && echo "template JSON ok"
