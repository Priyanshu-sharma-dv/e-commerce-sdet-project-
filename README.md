# E-Commerce Quality Engineering & SDET Automation Platform

A production-style Python SDET portfolio project covering UI, API, database, integration, CI/CD, quality gates, and security scanning.

## Stack

Python 3.12, Pytest, Playwright, Selenium 4, HTTPX, Pydantic, PostgreSQL, SQLAlchemy/psycopg, Docker, GitHub Actions, Jenkins, Allure, pytest-xdist, pytest-rerunfailures, Ruff, Pyright, OWASP ZAP.

## Architecture

```text
UI -> Playwright/Selenium -> Pytest
API -> HTTPX -> Pytest -> Pydantic contracts
DB -> SQLAlchemy/psycopg -> PostgreSQL
                 |
                 v
       Integration validation
                 |
      GitHub Actions / Jenkins
        |       |        |
      Ruff   Pyright    Tests
                 |
             Docker/ZAP
```

## Framework practices

- Page Object Model and semantic Playwright locators
- Reusable Pytest fixtures
- API client abstraction
- Authenticated client/token handling
- Pydantic response-contract validation
- Parametrized negative tests
- PostgreSQL validation
- Failure screenshots and structured logs
- Parallel execution with pytest-xdist
- Retry support for explicitly marked flaky tests
- Coverage and quality gates
- CI artifacts and JUnit/Allure-compatible results
- OWASP ZAP baseline scanning

## Commands

```bash
pip install -r requirements.txt
playwright install chromium
pytest -v
pytest -m smoke -v
pytest -m regression -n auto -v
pytest --cov=app --cov=api_clients --cov=database --cov-report=term-missing
ruff check .
pyright
```

## Docker

```bash
docker compose up -d db app
docker compose run --rm playwright
```

## CI

GitHub Actions runs linting, type checking, parallel tests, coverage and stores artifacts. Jenkins runs the same quality flow plus the security stage.

## Interview talking points

1. Why Page Object Model?
2. Why Playwright for primary UI automation and Selenium as secondary coverage?
3. How do Pytest fixtures control test dependencies and scope?
4. How is authentication reused without duplicating login logic?
5. How do API contract models detect breaking changes?
6. How does UI/API/DB integration testing differ from unit testing?
7. How does parallel execution affect test isolation?
8. How are flaky tests handled without hiding genuine failures?
9. What does the CI quality gate protect?
10. What does an OWASP ZAP baseline scan provide and what does it not prove?
