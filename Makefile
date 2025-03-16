PHONY: check
check:
	black .
	isort .
	flake .

PHONY: test
test:
	pytest . -v