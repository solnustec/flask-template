help:
	@grep -E '^[A-Za-z0-9_.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "[36m%-30s[0m %s\n", $$1, $$2}'

#
# Management commands
#
lint:
	black .
	isort . --profile black
	flake8 .

lint-check:
	black . --check
	isort . --check-only --profile black
	flake8 .

#
# Run before push to github
#

pre-push-fix:  ## Fix most of backend conflicts
	./scripts/pre_push_fix.sh


pre-push:  ## Check backend code
	./scripts/pre_push.sh
