output "network_name" {
  description = "Name of the Docker network created by Terraform"
  value       = docker_network.terraform_lab.name
}

output "container_name" {
  description = "Name of the Nginx container created by Terraform"
  value       = docker_container.nginx_lab.name
}

output "nginx_url" {
  description = "Local URL exposed by the Nginx container"
  value       = "http://localhost:${var.external_port}"
}
