#!/bin/bash

docker compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.override.local.yml up --build -d