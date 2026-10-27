# because of dotnet, we always build on amd64, and target platforms in cli
# dotnet doesn't support QEMU for building or running. 
# (errors common in arm/v7 32bit) https://github.com/dotnet/dotnet-docker/issues/1537
# https://hub.docker.com/_/microsoft-dotnet
# hadolint ignore=DL3029
# to build for a different platform than your host, use --platform=<platform>
# for example, if you were on Intel (amd64) and wanted to build for ARM, you would use:
# docker buildx build --platform "linux/arm64/v8" .

# build compiles the program for the builder's local platform. The default
# keeps plain `docker build` working when BuildKit's automatic platform args
# are unavailable; BuildKit overrides it for cross-platform builds.
ARG BUILDPLATFORM=linux/amd64
FROM --platform=${BUILDPLATFORM} mcr.microsoft.com/dotnet/sdk:10.0 AS build
ARG TARGETPLATFORM=linux/amd64
ARG TARGETARCH=amd64
ARG BUILDPLATFORM
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM"

WORKDIR /source
COPY *.csproj .
RUN dotnet restore -a $TARGETARCH

COPY . .
RUN dotnet publish -c release -o /app -a $TARGETARCH --self-contained false --no-restore

# app image
FROM mcr.microsoft.com/dotnet/runtime:10.0
LABEL org.opencontainers.image.source="https://github.com/0x52616469616e74/example-voting-app"
WORKDIR /app
COPY --from=build /app .
USER $APP_UID
ENTRYPOINT ["dotnet", "Worker.dll"]
