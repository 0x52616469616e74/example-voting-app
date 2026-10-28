# Cloud cleanup evidence

Captured on 2026-10-28 in `us-east-1`, after the Capstone 1 rollback demo and
the Capstone 2 incident drill had both been recorded on the same cluster.
Account identifiers are redacted.

## Order of operations

1. `helm uninstall` for `robot-shop`, `voting-app`, `monitoring`, `loki`,
   `fluent-bit` and `jaeger`, so Kubernetes deleted its AWS load balancer and
   EBS-backed volumes before the VPC was removed.
2. `aws eks delete-nodegroup --nodegroup-name capstone-free`. This Free-Tier
   node group was created outside Terraform (see
   [03-terraform-eks.md](03-terraform-eks.md)), so it was removed explicitly
   (11:00:21 → 11:08:31 UTC).
3. `terraform plan -destroy -out=destroy.tfplan`, reviewed, then
   `terraform apply destroy.tfplan`.

```text
terraform plan -destroy
Plan: 0 to add, 0 to change, 38 to destroy.

terraform apply destroy.tfplan   (2026-10-28T11:08:49Z → 11:12:17Z)
Apply complete! Resources: 0 added, 0 changed, 38 destroyed.

Terraform state resources remaining: 0
```

## Leftover check (AWS CLI, us-east-1)

```text
EKS clusters: 0
EC2 instances (pending/running/stopping/stopped): 0
Classic load balancers: 0
ALB/NLB load balancers: 0
Unattached EBS volumes: 0
NAT gateways (available/pending): 0
Elastic IPs: 0
Non-default VPCs: 0
EKS CloudWatch log groups: 0
KMS keys pending deletion: 0 alias(es) remaining
```

## Recreating the environment

The same configuration recreates the cluster from code:

```bash
cd terraform
terraform init
terraform plan -var 'cluster_endpoint_public_access_cidrs=["<your-ip>/32"]' -out=capstone.tfplan
terraform apply capstone.tfplan
aws eks update-kubeconfig --region us-east-1 --name radiant-o-capstone
helm upgrade --install voting-app ./voting-app \n  --namespace voting-app --create-namespace \n  --set global.imageTag=<git-sha> \n  --set-string postgresql.auth.password='<strong-password>' \n  --wait --timeout 10m
```
