# DevOps Capstone 1 — Example Voting App

[![Capstone CI/CD](https://github.com/Radiant-O/example-voting-app/actions/workflows/capstone-ci.yml/badge.svg)](https://github.com/Radiant-O/example-voting-app/actions/workflows/capstone-ci.yml)

This repository turns Docker's Example Voting App into a reproducible DevOps delivery project. It runs locally with Docker Compose, provisions Amazon EKS with Terraform, packages the application with Helm, scans source and images with Trivy, and publishes immutable images to GitHub Container Registry (GHCR).

## Architecture

```text
Browser -> vote (Python) -> Redis -> worker (.NET) -> PostgreSQL -> result (Node.js) -> Browser
```

The application has two web front ends, one background worker, and two stateful data services. See [docs/architecture.md](docs/architecture.md) for runtime and delivery diagrams.

## Repository layout

| Path | Purpose |
| --- | --- |
| `vote/`, `result/`, `worker/` | Application source and hardened container images |
| `docker-compose.yml` | Local development stack |
| `terraform/` | EKS infrastructure as code |
| `voting-app/` | Helm chart for Kubernetes |
| `.github/workflows/capstone-ci.yml` | Validation, security scanning, image publishing, and optional EKS deployment |
| `docs/` | Architecture, security, rollback, and evidence guidance |

## Run locally

Prerequisites: Docker Desktop with the Linux container engine running.

```bash
docker compose up --build
```

- Vote: <http://localhost:8080>
- Results: <http://localhost:8081>

Stop the stack with:

```bash
docker compose down -v
```

The `-v` flag removes the local development volumes, including database data.

## Container security

- Runtime base images are pinned to specific versions.
- Application containers run as unprivileged users.
- Build contexts exclude local dependencies, credentials, and infrastructure state.
- Kubernetes containers drop Linux capabilities, disable privilege escalation, and use read-only root filesystems where practical.
- Trivy scans both the repository and every built image for high and critical findings.

See [docs/security.md](docs/security.md) for the threat model and remediation workflow.

## Provision Amazon EKS

> EKS and its worker nodes cost money. Destroy the environment when it is not being used.

Install Terraform and the AWS CLI, authenticate to the intended AWS account, then run:

```bash
cd terraform
terraform init
terraform plan -out=tfplan
terraform apply tfplan
aws eks update-kubeconfig --region us-east-1 --name radiant-o-capstone
```

Copy `terraform/terraform.tfvars.example` to `terraform.tfvars` only when overriding defaults. Terraform state, plans, and environment files are excluded from Git.

## CI/CD

On pushes and pull requests, GitHub Actions validates application syntax, Docker Compose, Terraform, and Helm, then scans the repository. On pushes to `main`, it also builds and scans all three application images and publishes them as:

```text
ghcr.io/radiant-o/example-voting-app-vote:<git-sha>
ghcr.io/radiant-o/example-voting-app-result:<git-sha>
ghcr.io/radiant-o/example-voting-app-worker:<git-sha>
```

The deployment job remains safely disabled until these GitHub Actions variables are configured:

| Name | Type | Purpose |
| --- | --- | --- |
| `AWS_REGION` | Variable | Region containing the EKS cluster |
| `EKS_CLUSTER_NAME` | Variable | Terraform-created cluster name |
| `AWS_ROLE_ARN` | Variable | IAM role trusted by GitHub OIDC |
| `POSTGRES_PASSWORD` | Secret | Database password supplied to Helm |

The workflow uses GitHub OIDC, so no long-lived AWS access keys are stored in GitHub.

GHCR creates new personal container packages as private. After the first successful build, make the three packages public in GitHub package settings so EKS can pull them anonymously. The source label in each image links the package to this repository before publication.

## Deploy with Helm

For a manual deployment, use the immutable commit SHA produced by CI:

```bash
helm upgrade --install voting-app ./voting-app \
  --namespace voting-app --create-namespace \
  --set global.imageTag=<git-sha> \
  --set-string postgresql.auth.password='<strong-password>' \
  --wait --timeout 10m

kubectl port-forward --namespace voting-app service/vote 8080:80
kubectl port-forward --namespace voting-app service/result 8081:80
```

Never commit a real database password. In a production environment, replace the chart-managed Secret with AWS Secrets Manager plus an external-secrets controller.

## Rollback and evidence

- Follow [docs/rollback-demo.md](docs/rollback-demo.md) to demonstrate a failed release and Helm rollback.
- Use [docs/evidence/README.md](docs/evidence/README.md) as the submission evidence checklist.
- Keep screenshots free of passwords, tokens, account IDs, and other secrets.

## Cleanup

```bash
helm uninstall voting-app --namespace voting-app
cd terraform
terraform destroy
```

Confirm in AWS that the EKS cluster and related load balancers or volumes are gone.

## Capstone 2

Capstone 2 is maintained separately in the [Radiant-O/robot-shop](https://github.com/Radiant-O/robot-shop) fork so that its observability platform and evidence remain independent from this delivery project.
