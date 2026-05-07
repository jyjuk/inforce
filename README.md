# Lunch Voting

Internal service for employees to vote on where to have lunch. Restaurants upload daily menus via API, employees vote through a mobile app.

## Stack

- Python 3.13, Django 6, Django REST Framework
- PostgreSQL
- JWT authentication (djangorestframework-simplejwt)
- Docker + docker-compose
- pytest

## Running with Docker

```bash
cp .env.example .env
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

On first run migrations are applied automatically.

To create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

## Running locally

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env         # set DATABASE_URL to sqlite:///db.sqlite3 for local dev
python manage.py migrate
python manage.py runserver
```

## Running tests

```bash
pytest
```

## Interactive API documentation

Swagger UI is available at `http://localhost:8000/api/docs/` — all endpoints can be explored and tested directly in the browser.

## API endpoints

| Method | URL | Description | Auth |
|--------|-----|-------------|------|
| POST | `/api/auth/login/` | Obtain JWT token | — |
| POST | `/api/auth/refresh/` | Refresh JWT token | — |
| POST | `/api/restaurants/` | Create restaurant | Admin |
| POST | `/api/restaurants/menu/` | Upload menu for today | Admin |
| GET  | `/api/restaurants/menu/today/` | Get today's menus | JWT |
| POST | `/api/employees/` | Create employee | Admin |
| POST | `/api/voting/` | Vote for a menu | JWT |
| GET  | `/api/voting/results/` | Get today's results | JWT |

## API versioning

The results endpoint supports two response formats based on the `Build-Version` header:

- `Build-Version: 1` (or absent) — returns the winning restaurant only
- `Build-Version: 2` — returns all restaurants ranked by vote count
