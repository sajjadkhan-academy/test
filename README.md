# IDP Templates - Python Service

## Directory Structure

```
idp-templates-wip/
├── .github/
│   └── workflows/
│       ├── ci.yml        # Code quality & security checks
│       └── cd.yml         # Build & publish Docker image
└── python-service/
    ├── main.py            # FastAPI application
    ├── requirements.txt   # Python dependencies
    ├── Dockerfile         # Container definition
    ├── .dockerignore      # Docker ignore rules
    ├── .gitignore         # Git ignore rules
    ├── .flake8            # Flake8 configuration
    ├── .mypy.ini          # mypy configuration
    ├── pyproject.toml     # Black & Bandit config
    └── README.md          # Documentation
```

## What This Template Includes

### 1. CI/CD Workflows

#### CI Workflow (`.github/workflows/ci.yml`)
- **Code Quality**: Black formatter, Flake8 linter, mypy type checker
- **Security Scanning**: Bandit security linter, Safety vulnerability check
- **Secret Detection**: GitGuardian, TruffleHog
- **Docker Security**: Trivy vulnerability scanning

#### CD Workflow (`.github/workflows/cd.yml`)
- **Build**: Docker image with buildx
- **Push**: Automatically to GitHub Container Registry (GHCR)
- **Attestations**: Build provenance signing
- **Caching**: Layer caching for faster builds

### 2. Python Service
- FastAPI framework
- Health check endpoints
- Docker support
- Security best practices (non-root user)

## How to Push This to GitHub

### Step 1: Initialize Git Repository

```bash
cd idp-templates-wip
git init
git add .
git commit -m "Initial commit: Python service with CI/CD"
```

### Step 2: Add Remote Repository

```bash
git remote add origin https://github.com/sajjadkhan-academy/idp-templates.git
```

### Step 3: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

## What Happens When You Use This Template

When a user creates a Python service from the IDP dashboard:

1. **Repository Created**: New repo in `sajjadkhan-academy` org
2. **Files Copied**: All template files including `.github/workflows/`
3. **First Push**: User makes initial commit
4. **CI/CD Triggered**: GitHub Actions automatically run
5. **Image Built**: Docker image pushed to GHCR

## Workflow Features

### CI Pipeline
```
On: Pull Request or Push to main/develop
├─ Code Quality Checks
│  ├─ Black formatting check
│  ├─ Flake8 linting
│  └─ mypy type checking
├─ Security Scanning
│  ├─ Bandit (security linter)
│  └─ Safety (known vulnerabilities)
├─ Secret Detection
│  ├─ GitGuardian
│  └─ TruffleHog
└─ Docker Security
   └─ Trivy vulnerability scan
```

### CD Pipeline
```
On: Push to main branch or version tags
├─ Checkout code
├─ Set up Docker Buildx
├─ Login to GHCR
├─ Extract metadata (tags, labels)
├─ Build & push Docker image
└─ Generate attestations
```

## Docker Image Location

Images will be available at:
```
ghcr.io/sajjadkhan-academy/<repository-name>:<tag>
```

Tags:
- `latest` (main branch)
- `main` (branch name)
- `sha-<commit-sha>` (specific commit)
- `v1.0.0` (semantic version tags)

## Testing Locally

Before pushing, you can test the service:

```bash
cd python-service

# Run locally
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

# Test with Docker
docker build -t python-service:test .
docker run -p 8000:8000 python-service:test
```

## Notes

- Workflows will run automatically on push
- No secrets need to be configured (uses GITHUB_TOKEN)
- All security scanning is automated
- Images are automatically published to GHCR

## Next Steps

1. Push this template to GitHub
2. Create a service through IDP dashboard
3. Watch the CI/CD pipeline run
4. Image will be available in GHCR

