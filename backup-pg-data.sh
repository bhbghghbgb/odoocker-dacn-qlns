#!/bin/bash

docker run --rm \
  -v dacn-backup:/archive \
  -v odoocker_pg-data:/backup/odoocker-dacn-qlns-backup:ro \
  --entrypoint backup \
  offen/docker-volume-backup:v2