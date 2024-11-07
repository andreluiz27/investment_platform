# Makefile for Python project with Docker Compose

# Variables
DOCKER_COMPOSE = docker-compose
PYTHON = python3

# Default target
.PHONY: help
help:
	@echo "Makefile commands:"


# Start services
.PHONY: api
api:
	$(DOCKER_COMPOSE) up -d --build

# Initialize database
.PHONY: init-database
init-database:
	echo 'CREATE DATABASE IF NOT EXISTS toro_test_db' | docker exec -i toro_db /usr/bin/mysql -u root --password=mypass && $(DOCKER_COMPOSE) up -d --build

# Load mocked database
.PHONY: load-mocked-db
load-mocked-db:
	cat mocked_db.sql | docker exec -i toro_db /usr/bin/mysql -u root --password=mypass toro_test_db
