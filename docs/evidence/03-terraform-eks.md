# Terraform and EKS evidence

Captured on 2026-10-28 in `us-east-1` with credentials and account identifiers
redacted.

```text
Terraform v1.16.6
terraform init: successful
terraform validate: Success! The configuration is valid.
Terraform-managed resources in state: 54

Cluster
name: radiant-o-capstone
status: ACTIVE
version: 1.36
private endpoint: enabled
public endpoint: enabled, restricted to the operator /32

Managed node group
name: capstone-free
status: ACTIVE
instance type: m7i-flex.large
desired nodes: 1

kubectl get nodes
STATUS  VERSION
Ready   v1.36.5-eks-577a51e
```

AWS rejected the originally planned `t3.large` as ineligible for this new
account's Free Tier. The validated Terraform default was changed to
`m7i-flex.large`, the instance type AWS reported as eligible. The node group
used for the time-bounded demonstration was created with the same Terraform
provisioned cluster IAM role and subnets. This exception is recorded rather
than misrepresented as an uninterrupted Terraform apply.

