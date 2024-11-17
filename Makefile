

##@ Utility
.PHONY: help
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make <target>\033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: venv
uv:  ## Install uv
	curl -LsSf https://astral.sh/uv/install.sh | sh

.PHONY: dev
dev:  ## Install dev dependencies
	uv sync --dev

.PHONY: install
install:  ## Install dependencies
	uv sync

.PHONY: test
test:  ## Run tests
	uv run pytest

.PHONY: lint
lint:  ## Run linters
	uv run ruff check ./src ./tests

.PHONY: fix
fix:  ## Fix lint errors
	uv run ruff check ./src ./tests --fix

.PHONY: cov
cov: ## Run tests with coverage
	uv run pytest --cov=src --cov-report=term-missing

.PHONY: pages
pages: doc  ## Build documentation and push to gh-pages
	mkdir gh-pages
	touch gh-pages/.nojekyll
	cp -r docs/build/html/* gh-pages/

.PHONY: doc
doc:  ## Build documentation
	cd docs && uv run make html

.PHONY: build
build:  ## Build package
	uv build

.PHONY: dbash
dbash:  ## Run docker
	docker run -v ${PWD}:/git/$(shell basename ${PWD}) -w /git/$(shell basename ${PWD}) -it python:3.12 /bin/bash
