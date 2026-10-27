# base defines a base stage that uses the official python runtime base image
FROM python:3.13.17-slim-bookworm AS base

# Add curl for healthcheck
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Set the application directory
WORKDIR /usr/local/app

RUN groupadd --gid 10001 app && \
    useradd --uid 10001 --gid app --create-home --shell /usr/sbin/nologin app

# Install our requirements.txt
COPY requirements.txt ./requirements.txt
RUN python -m pip install --no-cache-dir --upgrade \
      pip \
      setuptools \
      urllib3==2.8.0 \
      msgpack==1.2.1 && \
    pip install --no-cache-dir -r requirements.txt

# dev defines a stage for development, where it'll watch for filesystem changes
FROM base AS dev
RUN pip install --no-cache-dir watchdog==6.0.0
ENV FLASK_ENV=development \
    PORT=8080
USER 10001:10001
CMD ["python", "app.py"]

# final defines the stage that will bundle the application for production
FROM base AS final

LABEL org.opencontainers.image.source="https://github.com/0x52616469616e74/example-voting-app"

# Copy our code from the current folder to the working directory inside the container
COPY --chown=10001:10001 . .

# Make port 80 available for links and/or publish
EXPOSE 8080

ENV PORT=8080

USER 10001:10001

# Define our command to be run when launching the container
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
