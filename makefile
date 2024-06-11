COMPOSE_FILE := docker-compose.yaml

.PHONY: build-project start-project stop-project

build-project:
	@docker compose -f $(COMPOSE_FILE) build

start-project:
	@docker compose -f $(COMPOSE_FILE) up -d

stop-project:
	@docker compose -f $(COMPOSE_FILE) down