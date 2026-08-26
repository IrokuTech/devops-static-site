terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 4.5"
    }
  }
}

provider "docker" {}

resource "docker_network" "terraform_lab" {
  name = var.network_name
}

data "docker_registry_image" "nginx" {
  name = var.nginx_image
}

resource "docker_image" "nginx" {
  name          = data.docker_registry_image.nginx.name
  pull_triggers = [data.docker_registry_image.nginx.sha256_digest]
}

resource "docker_container" "nginx_lab" {
  name  = var.container_name
  image = docker_image.nginx.image_id

  networks_advanced {
    name = docker_network.terraform_lab.name
  }

  ports {
    internal = 80
    external = var.external_port
  }
}
