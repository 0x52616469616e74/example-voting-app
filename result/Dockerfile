FROM node:22.23.2-bookworm-slim AS base

# add curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl tini && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/app

COPY package*.json ./

RUN npm ci && \
 npm cache clean --force && \
 mv /usr/local/app/node_modules /node_modules

FROM base AS dev

RUN npm install -g nodemon@3.1.10

COPY --chown=node:node . .

ENV PORT=8080
EXPOSE 8080

USER node

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["nodemon", "--inspect=0.0.0.0", "server.js"]

FROM base AS final

LABEL org.opencontainers.image.source="https://github.com/Radiant-O/example-voting-app"

COPY --chown=node:node . .

ENV PORT=8080
EXPOSE 8080

USER node

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["node", "server.js"]
