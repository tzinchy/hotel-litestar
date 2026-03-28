.PHONY: run-infra
.PHONY: stop-infra
.PHONY: app
.PHONY: src-file

run-infra:
	docker-compose up -d

stop-infra:
	docker-compose down

app:
	uv run uvicorn src.main:app --reload

#filename=name make src-file
src-file:
	uv run python -m src.${filename}
