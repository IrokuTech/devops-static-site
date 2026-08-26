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
  name = "terraform-lab-network"
}

resource "docker_image" "nginx" {
  name = "nginx:alpine"
}

resource "docker_container" "nginx_lab" {
  name  = "terraform-nginx-lab"
  image = docker_image.nginx.image_id

  networks_advanced {
    name = docker_network.terraform_lab.name
  }

  ports {
    internal = 80
    external = 8081
  }
}
