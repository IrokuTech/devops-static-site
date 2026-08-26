variable "network_name" {
  description = "Name of the Docker network managed by Terraform"
  type        = string
  default     = "terraform-lab-network"
}

variable "container_name" {
  description = "Name of the Nginx container managed by Terraform"
  type        = string
  default     = "terraform-nginx-lab"
}

variable "nginx_image" {
  description = "Docker image used by the Nginx container"
  type        = string
  default     = "nginx:alpine"
}

variable "external_port" {
  description = "Host port exposed by the Nginx container"
  type        = number
  default     = 8081
}
