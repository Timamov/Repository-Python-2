PHONY: check
check:
	echo '1234'
	black .
	isort .
	flake8 .

PHONY: test
test:
	echo 'tests started...'
	pytest . -v