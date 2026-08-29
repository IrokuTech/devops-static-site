# DevOps Static Site

A portfolio project built to demonstrate professional Git workflows, CI/CD, containerisation, multi-service orchestration, reverse proxy configuration, Infrastructure as Code, local Kubernetes orchestration, and automated hosting through GitHub Pages.

The frontend remains intentionally simple so that the project can focus on DevOps practices and infrastructure concepts rather than application complexity.

---

## Live Demo

🌐 https://irokutech.github.io/devops-static-site/

---

## Project Goals

This project was created to practice and demonstrate:

- Working in a Linux development environment (WSL2 + Ubuntu)
- Version control with Git
- Feature branch workflow
- Pull Requests
- SSH authentication with GitHub
- Continuous Integration and Continuous Deployment (CI/CD)
- GitHub Actions workflows
- GitHub Pages deployments
- Technical documentation and project organization

The objective is not to build a complex frontend application, but to show a clean and reproducible development workflow similar to what is commonly used in professional software teams.

---

## Technologies

| Category | Technologies |
|----------|--------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| Database | PostgreSQL |
| Web Server | Nginx |
| Containerisation | Docker, Docker Compose |
| Version Control | Git |
| Repository Hosting | GitHub |
| CI/CD | GitHub Actions |
| Deployment | GitHub Pages |
| Development Environment | WSL2, Ubuntu 24.04, Visual Studio Code |
| Infrastructure as Code | Terraform |
| Container Orchestration | Kubernetes, kubectl, Kind |

---

## Repository Structure

```text
devops-static-site/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── api/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── site/
│   ├── assets/
│   │   ├── images/
│   │   └── icons/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── .terraform.lock.hcl
│
├── kubernetes/
│   ├── README.md
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── secret.example.yaml
│
├── Dockerfile
├── nginx.conf
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

The repository separates deployment configuration from the website source code.

Only the contents of the `site/` directory are published to GitHub Pages.

---

## Architecture

```text
Developer
      │
      ▼
Feature Branch
      │
      ▼
Git Commit
      │
      ▼
GitHub Push
      │
      ▼
Pull Request
      │
      ▼
Merge to main
      │
      ▼
GitHub Actions
      │
      ▼
Build & Package site/
      │
      ▼
GitHub Pages
      │
      ▼
Public Website
```

---

## CI/CD Pipeline

The deployment pipeline is fully automated.

Every push merged into the `main` branch triggers a GitHub Actions workflow that:

1. Checks out the repository.
2. Configures GitHub Pages.
3. Packages the `site/` directory.
4. Uploads the Pages artifact.
5. Deploys the website automatically.

The workflow also supports manual execution using `workflow_dispatch`.

---

## Local Docker Compose Architecture

```text
Client
  │
  │ localhost:8080
  ▼
Nginx
  │
  ├── /              → Static portfolio files
  │
  ├── /health ───────┐
  │                  │
  └── /api/* ────────┤
                     ▼
                 Flask API
                   :8000
                     │
                     ▼
                 PostgreSQL
                   :5432
                     │
                     ▼
              Persistent volume
```

Docker Compose orchestrates three services on a shared internal network:

- `frontend` — Nginx serves the static portfolio and acts as the reverse proxy.
- `api` — Flask provides the application endpoints.
- `db` — PostgreSQL stores the persistent visit counter.

Nginx is the only service exposed to the host for application traffic, through `localhost:8080`. The Flask API listens on port `8000` inside the Docker network but is not published directly to the host.

Requests to `/` are served directly by Nginx from the static site. Requests to `/health` and `/api/*` are forwarded to the Flask service using Docker Compose service discovery at `api:8000`.

The reverse proxy forwards the `Host`, `X-Real-IP`, `X-Forwarded-For`, and `X-Forwarded-Proto` headers so that the backend receives information about the original client request.

The Flask API connects to PostgreSQL using the `db` service name. PostgreSQL stores its data in a named volume so that the visit counter survives container recreation.

PostgreSQL uses a healthcheck together with a conditional `depends_on` configuration so that the API waits for the database to become healthy. The frontend also depends on the API for startup ordering; this dependency does not provide an API readiness guarantee.

---

## Git Workflow

Development follows a feature branch strategy.

```text
main
 │
 ├── feature/homepage
 ├── feature/github-pages-deploy
 ├── feature/readme-documentation
 ├── feature/docker-introduction
 ├── feature/docker-compose
 ├── feature/nginx-reverse-proxy
 ├── feature/terraform-introduction
 └── feature/kubernetes-introduction
```

Typical workflow:

```text
Create feature branch
        ↓
Develop changes
        ↓
Commit
        ↓
Push
        ↓
Open Pull Request
        ↓
Review changes
        ↓
Merge into main
        ↓
Automatic deployment
```

Direct development on `main` is intentionally avoided.

---

## Running the Project Locally

Clone the repository:

```bash
git clone git@github.com:IrokuTech/devops-static-site.git
```

Move into the project:

```bash
cd devops-static-site
```

Open it in Visual Studio Code:

```bash
code .
```

Launch the website using the **Live Server** extension or open:

```text
site/index.html
```

---

## Running with Docker

Build the Docker image:

```bash
docker build -t devops-static-site:v1 .
```

Run the container:

```bash
docker run -d \
  --name devops-static-site \
  -p 8080:80 \
  devops-static-site:v1
```

Open the website:

```text
http://localhost:8080
```

Stop the container:

```bash
docker stop devops-static-site
```

Remove the container:

```bash
docker rm devops-static-site
```

The application is served by an Nginx container using the official `nginx:alpine` image.

## Running with Docker Compose

The complete local stack consists of three services:

- Nginx frontend
- Flask API
- PostgreSQL database

Build and start the stack:

```bash
docker compose up --build -d
```

Check the service status:

```bash
docker compose ps
```

The frontend is available at:

```text
http://localhost:8080
```

Check the API health endpoint through Nginx:

```bash
curl http://localhost:8080/health
```

Increment and retrieve the persistent visit counter through Nginx:

```bash
curl http://localhost:8080/api/visits
```

The Flask API is intentionally not published directly to the host. Application traffic reaches it through the Nginx reverse proxy and the internal Docker Compose network.

Validate the Nginx configuration:

```bash
docker compose exec frontend nginx -t
```

Inspect the complete Nginx configuration loaded inside the container:

```bash
docker compose exec frontend nginx -T
```

View Nginx and API logs:

```bash
docker compose logs frontend
docker compose logs api
```

View service logs:

```bash
docker compose logs
```

Stop and remove the containers and Compose network:

```bash
docker compose down
```

The PostgreSQL data is stored in a named Docker volume and is preserved by `docker compose down` unless the volume is explicitly removed.

---

## Terraform Lab

The repository includes a local Terraform lab for practicing Infrastructure as Code concepts with Docker.

This lab is intentionally independent from the main Docker Compose application stack. Terraform manages its own Nginx container and Docker network for learning purposes; it does not manage the Flask, PostgreSQL, or Nginx services defined in `compose.yaml`.

Initialize the Terraform working directory:

```bash
cd terraform
terraform init
```

Format and validate the configuration:

```bash
terraform fmt
terraform validate
```

Preview the infrastructure changes:

```bash
terraform plan
```

Create the lab infrastructure:

```bash
terraform apply
```

The default Nginx endpoint is:

```text
http://localhost:8081
```

Inspect the Terraform-managed resources and outputs:

```bash
terraform state list
terraform output
```

Input variables can override the default configuration without modifying the Terraform source files. For example:

```bash
terraform plan -var="external_port=9090"
```

Destroy the Terraform-managed lab infrastructure:

```bash
terraform destroy
```

Local Terraform state and provider files are excluded from version control. The dependency lock file `.terraform.lock.hcl` is committed to keep provider selections reproducible.

The lab currently demonstrates:

- Terraform providers and provider version constraints
- Docker resources managed through Terraform
- Input variables and outputs
- Terraform state
- Implicit resource dependencies
- Data sources
- Docker registry image digest tracking with `pull_triggers`
- Infrastructure lifecycle with `plan`, `apply`, and `destroy`

---

## Kubernetes Local Lab

The repository includes a reproducible local Kubernetes lab using Kind.

This lab is intentionally independent from the Docker Compose and Terraform environments. It is designed to practise core Kubernetes concepts locally without requiring external cloud infrastructure.

The lab includes:

- A dedicated `devops-lab` Namespace
- A ConfigMap for application configuration
- A locally created Secret that is not committed to Git
- An Nginx Deployment with two replicas
- A ClusterIP Service
- Kubernetes DNS and service discovery
- EndpointSlice inspection
- Deployment rollout and rollback workflows
- Local access using `kubectl port-forward`

Create the Namespace and ConfigMap:

```bash
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/configmap.yaml
```

Create the Secret locally:

```bash
kubectl create secret generic nginx-secret \
  --from-literal=DEMO_PASSWORD='change-me' \
  -n devops-lab
```

Apply the Deployment and Service:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

Verify the Deployment and Service:

```bash
kubectl rollout status deployment/nginx-demo -n devops-lab
kubectl get pods -n devops-lab
kubectl get service nginx-service -n devops-lab
kubectl get endpointslice -n devops-lab
```

Access the Service locally:

```bash
kubectl port-forward service/nginx-service 8082:80 -n devops-lab
```

Then test it from another terminal:

```bash
curl http://localhost:8082
```

The lab was validated by deleting the `devops-lab` Namespace and rebuilding the complete environment from the documented procedure.

Real Kubernetes credentials are not committed to the repository. `kubernetes/secret.example.yaml` documents only the expected Secret structure.

---

## Current Status

✔ Linux development environment (WSL2)

✔ Git configured

✔ SSH authentication

✔ Professional Git workflow

✔ Pull Requests

✔ GitHub Actions deployment

✔ GitHub Pages hosting

✔ Docker containerisation

✔ Public website available

✔ Docker Compose multi-service orchestration

✔ Nginx reverse proxy

✔ Terraform Infrastructure as Code lab

✔ Terraform-managed Docker resources

✔ Terraform variables, outputs, state, and data sources

✔ Local Kubernetes lab with Kind

✔ Kubernetes Namespace, Deployment, Service, ConfigMap, and Secret management

✔ Kubernetes service discovery, rollout, rollback, and port-forwarding

✔ Reproducible Kubernetes environment reconstruction

✔ Internal API routing through Nginx

✔ Backend API isolated from direct host access

✔ Flask API

✔ PostgreSQL persistence

✔ Container healthcheck and service dependency

---

## Roadmap

Planned improvements include:

- Improve responsive design
- Accessibility enhancements
- Custom favicon
- Additional portfolio projects
- Monitoring stack

---

## Key Learning Outcomes

Throughout this project, the focus has been on understanding **why** each tool is used instead of simply making it work.

Some of the concepts practiced include:

- Git branching strategies
- Commit hygiene
- Pull Request workflow
- SSH authentication
- YAML workflow configuration
- GitHub Actions
- GitHub Pages
- CI/CD principles
- Docker image creation
- Container lifecycle management
- Deployment automation
- Technical documentation
- Docker Compose service orchestration
- Docker networking and service discovery
- Environment-based service configuration
- PostgreSQL persistence with named volumes
- Container healthchecks and startup dependencies
- Nginx reverse proxy configuration
- Reverse proxy routing
- Docker internal vs published ports
- Docker Compose service discovery
- Forwarded HTTP headers
- Nginx configuration validation and logs
- Infrastructure as Code principles
- Terraform provider and resource configuration
- Terraform state management
- Terraform plan, apply, and destroy lifecycle
- Terraform input variables and outputs
- Terraform implicit dependencies
- Terraform data sources
- Kubernetes cluster fundamentals
- Kubernetes Namespaces
- Deployments and ReplicaSets
- Kubernetes reconciliation
- Labels and selectors
- ClusterIP Services
- Kubernetes DNS and service discovery
- EndpointSlices
- ConfigMaps and Secrets
- Kubernetes logs and resource inspection
- Deployment rollout and rollback
- Local Kubernetes development with Kind
- Reproducible Kubernetes environment reconstruction

---

## License

This project is available for educational and portfolio purposes.
