#!/usr/bin/env bash
set -euo pipefail
ITERATIONS="${ITERATIONS:-100}"

get_random_poll_question() {
  # This will fail for any question that isn't question 1
  # because there is only one question.
  curl -L -o /dev/null http://localhost/polls/$(( ( RANDOM % 10 ) ))
}

post_random_choice() {
  choice_to_make=$(seq 1 2 | sort -R | head -1)
  curl -L -o /dev/null -X POST -F "choice=$choice_to_make" http://localhost/polls/1/vote
}

for _ in $(seq 1 "$ITERATIONS")
do
  get_random_poll_question
  post_random_choice
done
