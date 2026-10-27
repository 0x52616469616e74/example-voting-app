# Submission evidence checklist

Store screenshots in this directory using numbered, descriptive filenames. Redact secrets, tokens, AWS account IDs, and private URLs before committing any image.

| Evidence | Suggested filename |
| --- | --- |
| Successful local Compose build and healthy containers | `01-compose-healthy.png` |
| Vote and results pages | `02-local-application.png` |
| Terraform plan or successful EKS apply | `03-terraform-eks.png` |
| Successful CI validation and Trivy scans | `04-ci-security.png` |
| SHA-tagged packages in GHCR | `05-ghcr-images.png` |
| Helm release and healthy Kubernetes pods | `06-helm-release.png` |
| Application reached through Kubernetes | `07-eks-application.png` |
| Controlled deployment failure | `08-rollback-failure.png` |
| Helm history and restored healthy release | `09-rollback-recovery.png` |
| Terraform destroy completion | `10-cleanup.png` |

Also retain the GitHub Actions run URL and the exact Git commit SHA used for the demonstration.
