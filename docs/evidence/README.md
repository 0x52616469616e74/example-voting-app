# Submission evidence checklist

Store screenshots in this directory using numbered, descriptive filenames. Redact secrets, tokens, AWS account IDs, and private URLs before committing any image.

## Verified online evidence

- Public fork: [0x52616469616e74/example-voting-app](https://github.com/0x52616469616e74/example-voting-app)
- Successful push workflow: [Capstone CI/CD run 40650601726](https://github.com/0x52616469616e74/example-voting-app/actions/runs/40650601726)
- Demonstrated image revision: `e30553c367c3c9cddc4661050ebe234bc20af383`
- Public SHA-tagged images:
  - [Vote](https://github.com/users/0x52616469616e74/packages/container/package/example-voting-app-vote)
  - [Result](https://github.com/users/0x52616469616e74/packages/container/package/example-voting-app-result)
  - [Worker](https://github.com/users/0x52616469616e74/packages/container/package/example-voting-app-worker)

The workflow run above passed application tests, Docker Compose validation,
Terraform validation, Helm lint/template checks, repository Trivy scanning,
and build/Trivy/publish jobs for all three application images. A separate live
EKS demonstration is recorded below; long-lived cloud credentials were not
added to GitHub.

## Acceptance status

| Requirement | Status | Evidence or remaining action |
| --- | --- | --- |
| Forked repository | Done | Public fork linked above; GitHub records `dockersamples/example-voting-app` as its parent. |
| Local application | Done | [`docker compose ps` health record](01-compose-healthy.md), [Vote page](02a-vote-page.png), and [Result page](02b-result-page.png) show the live local flow. |
| Service flow | Done | See [`docs/architecture.md`](../architecture.md). |
| Container hardening | Done | Non-root runtime users, reduced runtime stages, `.dockerignore`, Kubernetes security contexts, and successful image rebuilds/scans. |
| Terraform code | Done with recorded exception | `terraform init`, validation, an AWS-backed apply, 54 state resources, and the Free-Tier node-group exception are recorded in [03-terraform-eks.md](03-terraform-eks.md). |
| Kubernetes connectivity | Done | [03-terraform-eks.md](03-terraform-eks.md) records an ACTIVE EKS 1.36 cluster and Ready node. |
| CI pipeline and Trivy | Done | Successful workflow linked above; repository and three image scan steps passed. |
| Images published | Done with registry substitution | Public GHCR packages use `main` and the full demonstrated commit SHA. The brief names Docker Hub, so confirm that GHCR is accepted or mirror the images to Docker Hub. |
| Helm chart | Done | [06-helm-release.md](06-helm-release.md) records the live release and five Ready workloads. |
| Working Kubernetes deployment | Done | [07-eks-application.md](07-eks-application.md) records HTTP checks and persisted votes across the complete service path. |
| Rollback demo | Done | [08-rollback-failure.md](08-rollback-failure.md) and [09-rollback-recovery.md](09-rollback-recovery.md) record the bad-image failure and recovery to the immutable SHA. |
| Documentation and diagram | Done | README, runtime/delivery diagrams, security rationale, Terraform guide, and rollback procedure are present. |
| Secrets safety | Done | CI secret/misconfiguration scan passed; no operational credentials are committed. |
| Cloud cleanup | Pending final shared demo | The cluster is temporarily retained for Capstone 2 evidence. Cleanup will be recorded after both demonstrations. |

All completed AWS items above are backed by real command output from the
temporary cluster; no AWS evidence was fabricated.

| Evidence | Suggested filename |
| --- | --- |
| Successful local Compose build and healthy containers | `01-compose-healthy.md` |
| Vote and results pages | `02a-vote-page.png`, `02b-result-page.png` |
| Terraform plan or successful EKS apply | `03-terraform-eks.png` |
| Successful CI validation and Trivy scans | `04-ci-security.png` |
| SHA-tagged packages in GHCR | `05-ghcr-images.png` |
| Helm release and healthy Kubernetes pods | `06-helm-release.png` |
| Application reached through Kubernetes | `07-eks-application.png` |
| Controlled deployment failure | `08-rollback-failure.png` |
| Helm history and restored healthy release | `09-rollback-recovery.png` |
| Terraform destroy completion | `10-cleanup.png` |

The run URL and exact demonstrated commit SHA are recorded above. Keep the
corresponding screenshots with the submission in case the online logs expire.
