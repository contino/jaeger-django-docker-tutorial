# django-jaeger-tutorial

A repo for learning how to use Jaeger with a simple Django polling app.

# Starting the demo

1. Start the Django stack: `docker-compose up -d website`
2. View the Jaeger console: `http://localhost:8080`
3. View the app: `http://localhost`

# Viewing the slides

1. Start the slides: `docker-compose up -d slides`
2. View the slides: `http://localhost:8000`. (NOTE: `$PWD/slides.md` must be present.)

# Breaking stuff

To impart some load on your simple webapp, run `scripts/load_runner.sh`. By default,
this will try to access questions in the poll (many won't exist, so you can see
what happens under failure) and cast some random votes.

This will run 100 times by default. To change this, simply run:

`ITERATIONS=$NUMBER_OF_ITERATIONS scripts/load_runner.sh`

While you're doing this, take a look at the Jaeger console at `http://localhost:8080`. You should
see latency data points and traces for each span (visit) recorded.

# Additional Notes

- Instead of configuring `app/website/settings.py` directly, this installation of Django uses an
  environment file for controlling its settings. The templatized version of it is located at
  `conf/website.yaml.tmpl`; the `generate-website-configs` Docker Compose service renders it.

  To recreate this file and reload Django, run `docker-compose restart generate-website-configs website`.

- In conjunction with the above, this implementation uses environment dotfiles to store
  sensitive information, such as the server `SECRET_KEY`. This makes this installation
  slightly more production-ready.

- To maintain a UNIX-like philosophy (do one thing; do it well), code for initializing
  tracing and databases lives in `app/website/{tracing, databases}.py`, respectively.

# Errata

- The Python `jaeger-client` is not compatible with OpenTracing v2 (despite its maintainer working
  on OpenTracing at Uber 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔). There is a
  [fork](https://github.com/mihau/jaeger-client-python/tree/feature/opentracing-2.0-support) and
  [pull request](https://github.com/jaegertracing/jaeger-client-python/pull/206) that fixes this,
  despite it failing PR tests. When this PR gets merged, the `requirements.txt` file will look
  slightly cleaner.
