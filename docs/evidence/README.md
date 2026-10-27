# Submission evidence checklist

Store screenshots in this directory using numbered, descriptive filenames. Redact secrets, tokens, AWS account IDs, and private URLs before committing any image.

## Verified online evidence

- Public fork: [0x52616469616e74/example-voting-app](https://github.com/0x52616469616e74/example-voting-app)
- Successful push workflow: [Capstone CI/CD run 40562052463](https://github.com/0x52616469616e74/example-voting-app/actions/runs/40562052463)
- Demonstrated source revision: `3a5f7815e260ad862e20832182e02fe6241439a1`
- Public SHA-tagged images:
  - [Vote](https://github.com/users/0x52616469616e74/packages/container/package/example-voting-app-vote)
  - [Result](https://github.com/users/0x52616469616e74/packages/container/package/example-voting-app-result)
  - [Worker](https://github.com/users/0x52616469616e74/packages/container/package/example-voting-app-worker)

The workflow run above passed application tests, Docker Compose validation,
Terraform validation, Helm lint/template checks, repository Trivy scanning,
and build/Trivy/publish jobs for all three application images. The EKS job was
intentionally skipped because no AWS account variables or credentials are
configured.

## Acceptance status

| Requirement | Status | Evidence or remaining action |
| --- | --- | --- |
| Forked repository | Done | Public fork linked above; GitHub records `dockersamples/example-voting-app` as its parent. |
| Local application | Done | [`docker compose ps` health record](01-compose-healthy.md), [Vote page](02a-vote-page.png), and [Result page](02b-result-page.png) show the live local flow. |
| Service flow | Done | See [`docs/architecture.md`](../architecture.md). |
| Container hardening | Done | Non-root runtime users, reduced runtime stages, `.dockerignore`, Kubernetes security contexts, and successful image rebuilds/scans. |
| Terraform code | Partial | `terraform init` and `terraform validate` pass in CI. A reviewed AWS-backed `terraform plan` is still required. |
| Kubernetes connectivity | Pending AWS | Requires real `kubectl get nodes` output showing Ready EKS nodes. |
| CI pipeline and Trivy | Done | Successful workflow linked above; repository and three image scan steps passed. |
| Images published | Done with registry substitution | Public GHCR packages use `main` and the full demonstrated commit SHA. The brief names Docker Hub, so confirm that GHCR is accepted or mirror the images to Docker Hub. |
| Helm chart | Partial | `helm lint` and `helm template` pass. A live deployed release still requires an EKS cluster. |
| Working Kubernetes deployment | Pending AWS | Requires a live vote reflected in Result through the Helm/EKS deployment. |
| Rollback demo | Pending AWS | Follow [`docs/rollback-demo.md`](../rollback-demo.md) against the live release and retain Helm history plus recovery evidence. |
| Documentation and diagram | Done | README, runtime/delivery diagrams, security rationale, Terraform guide, and rollback procedure are present. |
| Secrets safety | Done | CI secret/misconfiguration scan passed; no operational credentials are committed. |
| Cloud cleanup | Not applicable yet | No AWS resources were created. If EKS is provisioned, capture `terraform destroy` and confirm no billable leftovers. |

Do not mark the pending AWS items complete without real command output or
screenshots from the provisioned cluster.

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
