FROM python:3.13.17-slim-bookworm

# add apache bench (ab) tool
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    apache2-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /seed

RUN groupadd --gid 10001 app && \
    useradd --uid 10001 --gid app --create-home --shell /usr/sbin/nologin app

COPY --chown=10001:10001 . .

# create POST data files with ab friendly formats
RUN python make-data.py

USER 10001:10001

CMD ["/seed/generate-votes.sh"]
