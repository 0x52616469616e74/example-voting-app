# Security controls

## Container controls

- Version-pinned runtime images reduce unexpected changes between builds.
- Application processes run as non-root users.
- Multi-stage builds keep development tooling out of production images.
- `.dockerignore` files exclude Git metadata, local dependencies, secrets, and Terraform state.
- Kubernetes security contexts disable privilege escalation, drop all Linux capabilities, and use read-only root filesystems for application workloads.

## Pipeline controls

- Trivy scans the repository before image creation.
- Each application image is scanned before it is published.
- High or critical findings fail the workflow.
- GHCR authentication uses the short-lived workflow token.
- AWS deployment authentication uses GitHub OIDC and an IAM role; no static AWS credentials are required.
- Published image tags include the full Git commit SHA.

## Secret handling

No operational secret belongs in source control. The Helm chart's default password is an explicit placeholder and must be overridden at deployment. GitHub stores the password as an Actions secret. For a production implementation, use AWS Secrets Manager with External Secrets Operator or the Secrets Store CSI Driver and rotate the credential regularly.

## Finding workflow

1. Confirm whether the finding affects the runtime stage.
2. Upgrade the affected direct dependency or base image.
3. Rebuild and rerun the scan.
4. If no fix exists, document the affected component, exploitability, compensating controls, and a review date before considering a narrowly scoped exception.

Scanner suppressions must never be added only to make a pipeline green.

## Current limitations

- Redis and PostgreSQL are single replicas for demonstration purposes.
- Web services use port-forwarding by default; production ingress and TLS are environment-specific.
- NetworkPolicies and a managed database are recommended for production use.
- The default VPC is convenient for the capstone but is not a production network design.
