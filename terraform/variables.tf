variable "aws_region" {
  description = "AWS region in which to create the EKS cluster."
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Name of the EKS cluster."
  type        = string
  default     = "radiant-o-capstone"
}

variable "kubernetes_version" {
  description = "EKS Kubernetes minor version. Confirm it is in standard support before apply."
  type        = string
  default     = "1.36"
}

variable "environment" {
  description = "Environment tag applied to managed resources."
  type        = string
  default     = "capstone"
}

variable "node_instance_types" {
  description = "EC2 instance types used by the managed node group."
  type        = list(string)
  default     = ["t3.large"]
}

variable "node_min_size" {
  description = "Minimum managed node count."
  type        = number
  default     = 1
}

variable "node_max_size" {
  description = "Maximum managed node count."
  type        = number
  default     = 3
}

variable "node_desired_size" {
  description = "Initial managed node count. Two nodes are recommended for the observability capstone."
  type        = number
  default     = 2
}
