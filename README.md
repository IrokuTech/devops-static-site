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
├── site/
│   ├── assets/
│   │   ├── images/
│   │   └── icons/
│   │
│   ├── index.html
│   ├── style.css
│   └── script.js
│
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

## Current Status

✔ Linux development environment (WSL2)

✔ Git configured

✔ SSH authentication

✔ Professional Git workflow

✔ Pull Requests

✔ GitHub Actions deployment

✔ GitHub Pages hosting

✔ Public website available

---

## Roadmap

Planned improvements include:

- Improve responsive design
- Accessibility enhancements
- Custom favicon
- Additional portfolio projects
- Docker
- Docker Compose
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
- Deployment automation
- Technical documentation

---

## License

This project is available for educational and portfolio purposes.