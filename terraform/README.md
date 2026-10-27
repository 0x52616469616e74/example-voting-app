# EKS infrastructure

This Terraform configuration creates one Amazon EKS cluster and one managed node group in the account's default VPC. It deliberately does not run automatically from CI because creating and retaining these resources costs money.

## Validate without creating resources

```bash
terraform fmt -recursive
terraform init
terraform validate
terraform plan -out=capstone.tfplan
terraform show capstone.tfplan
```

Before `apply`, verify the AWS identity and region:

```bash
aws sts get-caller-identity
aws configure get region
```

## Create and connect

```bash
terraform apply capstone.tfplan
aws eks update-kubeconfig \
  --region "$(terraform output -raw aws_region)" \
  --name "$(terraform output -raw cluster_name)"
kubectl get nodes
```

## Destroy and verify cleanup

Delete application releases and any `LoadBalancer` Services first, then review the destruction plan:

```bash
helm uninstall voting-app --namespace voting-app
terraform plan -destroy
terraform destroy
```

Afterward, check the AWS console for leftover load balancers, volumes, snapshots, elastic IPs, and other billable resources. Never use `-auto-approve` for the first deployment or destruction.
