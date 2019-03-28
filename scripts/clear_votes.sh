#!/usr/bin/env sh
set -euo pipefail

for id in 1 2
do
  docker-compose exec database psql polls_app polls -c \
    "UPDATE polls_choice SET votes = 0 WHERE id = $id"
done
