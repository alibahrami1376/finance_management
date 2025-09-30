# Finance Management API (Django + DRF + JWT + PostgreSQL)

A lightweight API to manage income, expenses, and budgets.

## Features
- JWT auth (register/login)
- CRUD for Transactions & Budgets
- Per-user data isolation
- Simple budget overrun indicators
- Pytest test suite

## Quickstart

### 1) Create virtualenv & install deps
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
# source venv/bin/activate

pip install -r requirements.txt
```

### 2) Configure environment
Copy `.env.example` to `.env` and fill your values:

```
SECRET_KEY=dev-secret-change-me
DEBUG=1
ALLOWED_HOSTS=*
DB_NAME=financedb
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
```

> For local dev you can also omit DB_* vars and fallback to SQLite by setting `USE_SQLITE=1`.

### 3) Create Django project files
Project files are already included in this template. Just run migrations:

```bash
python manage.py migrate
```

### 4) Run server
```bash
python manage.py runserver
```

### 5) API endpoints
- `POST /api/auth/register/` → Create account
- `POST /api/auth/jwt/create/` → Obtain access/refresh
- `POST /api/auth/jwt/refresh/` → Refresh access token
- `GET/POST /api/transactions/` → List/Create
- `GET/PUT/PATCH/DELETE /api/transactions/{id}/`
- `GET/POST /api/budgets/`
- `GET/PUT/PATCH/DELETE /api/budgets/{id}/`

### 6) Run tests
```bash
pytest
```

## Optional: Docker Compose (not included by default)
You can add Docker later if needed.
