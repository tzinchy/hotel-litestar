.PHONY: run-infra
.PHONY: stop-infra

run-infra:
	docker-compose up -d

stop-infra:
	docker-compose down
