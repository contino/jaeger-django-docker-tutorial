FROM node:8-alpine
MAINTAINER Carlos Nunez <dev@carlosnunez.me>
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

RUN npm install -g reveal-md && mkdir /app
WORKDIR /app
ENTRYPOINT [ "reveal-md", "/app/slides.md", "--port", "8000", "--disable-auto-open" ]
