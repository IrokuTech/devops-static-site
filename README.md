# DevOps Static Site

A static portfolio website built to demonstrate a professional Git workflow, continuous deployment with GitHub Actions, and automated hosting through GitHub Pages.

The project intentionally uses only HTML, CSS and JavaScript to keep the focus on DevOps practices rather than frontend frameworks.

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
├── Dockerfile
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
Frontend
Nginx :80
   │
   │ Docker Compose network
   │
   ├──────────────┐
   │              │
   ▼              ▼
Flask API      PostgreSQL
:8000          :5432
   │              │
   └──────────────►
                  │
                  ▼
          Persistent volume
```

Docker Compose orchestrates the three local services using a shared network.

The Flask API connects to PostgreSQL using the `db` service name as its database host. PostgreSQL stores the visit counter in a named volume so that the data survives container recreation.

A database healthcheck is used together with `depends_on` to ensure that the API starts only after PostgreSQL is ready to accept connections.

---

## Git Workflow

Development follows a feature branch strategy.

```text
main
 │
 ├── feature/homepage
 │
 ├── feature/github-pages-deploy
 │
 └── feature/readme-documentation
 │
 └── feature/docker-introduction
 │
 └── feature/docker-compose
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

Check the API health endpoint:

```bash
curl http://localhost:8000/health
```

Increment and retrieve the persistent visit counter:

```bash
curl http://localhost:8000/api/visits
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
- Complete and merge Docker Compose phase
- Nginx
- Terraform
- Kubernetes
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

---

## License

This project is available for educational and portfolio purposes.