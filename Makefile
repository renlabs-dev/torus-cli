.PHONY: doc_run

doc_run:
	@echo "URL: http://localhost:8080/communex"
	pdoc -n ./src/communex
