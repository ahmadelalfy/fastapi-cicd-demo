# FastAPI CI/CD Demo

A minimal FastAPI project for learning continuous integration and deployment workflows.

## Project Structure

```
fastapi-cicd-demo/
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application
├── tests/
│   ├── __init__.py
│   └── test_health.py   # Health endpoint tests
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions CI pipeline
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Path     | Response                                      |
|--------|----------|-----------------------------------------------|
| GET    | `/`      | `{"message": "FastAPI CI/CD Demo is running"}` |
| GET    | `/health`| `{"status": "healthy"}`                       |

## Local Setup (Windows)

### 1. Create a virtual environment

Open PowerShell in the project root and run:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If you get an execution policy error, run this once (as Administrator or for your user):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Install requirements

With the virtual environment activated:

```powershell
pip install -r requirements.txt
```

### 3. Run the app

```powershell
uvicorn app.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 4. Run tests

```powershell
pytest
```

For verbose output:

```powershell
pytest -v
```

### 5. Run lint

```powershell
ruff check .
```

To auto-fix fixable issues:

```powershell
ruff check . --fix
```

## CI Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs automatically on:

- **Push** to `dev`, `qc`, or `main`
- **Pull requests** targeting `dev`, `qc`, or `main`

### Pipeline steps

1. **Checkout** — clones the repository
2. **Set up Python 3.11** — installs Python on `ubuntu-latest`
3. **Install dependencies** — runs `pip install -r requirements.txt`
4. **Lint** — runs `ruff check .` to enforce code style and catch common issues
5. **Test** — runs `pytest` to verify the `/health` endpoint works

If any step fails, the workflow fails and the PR or push is blocked from passing CI until the issue is fixed.

## Next Steps

- Push this repo to GitHub and open a pull request to see CI in action
- Add more endpoints and tests as you grow the project
- Extend the pipeline with coverage reports, deployment stages, or Docker (when ready)
Testing branch protection rules.
Direct push protection test.
