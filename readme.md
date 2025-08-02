# Flask PostgreSQL Alembic Template Application Example

## Installation and Launch

### Docker:

1. 
```bash
$ cd app
$ cp settings.yml.template settings.yml
```
2.

```bash
$ docker compose up
```

## Configuration

Go to app/ and open settings.yml file

You may configure loggers, change some settings constants for flask application under "flask" dict at yml

## Manage migrations by using alembic

```bash
$ ./manage_migrations.sh [make|upgrade|downgrade] [message_or_revision]
```

The command above allowing you to manage migrations through alembic:

1. Argument: action there are following options are avalaible: make, upgrade, downgrade
2. make - creates a migration
3. upgrade - applies migration
4. downgrade - revokes migration by 1 or by specified revision

## Enter to database:

### Docker

```bash
$ docker compose exec -it postgres psql -U user -d flask-postgres-alembic
```

## Project structure

### App directory

#### Description:
app/ directory contains source code. The structure is following:

- database - includes client that handles DB connection sessions at init py
    - models DB tables for application parts
- migrations contain Alembic migrations
- routes defines url routes that app handling
    - auth (/api/auth/{route})
        - schemes define validation schemes for requests
- services contain logic for app
    - auth - functions for auth business logic
- utils - contain different helpers for projects
    - database - contains helpers for database operations (healthcheck)

```bash
app/
├── alembic.ini
├── database
│   ├── __init__.py # DB client
│   └── models
│       ├── __init__.py
│       └── auth
│           └── __init__.py # User model
├── Dockerfile
├── main.py
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions # Here will be migrations files
├── requirements.txt
├── routes
│   ├── __init__.py
│   └── auth
│       ├── __init__.py # Routes for auth are defined here
│       └── schemes
│           └── __init__.py # Request payload validation is defined here
├── services
│   ├── __init__.py
│   └── auth
│       └── __init__.py # Functions and logic are defined here
├── settings.yml
├── settings.yml.template
└── utils
    ├── __init__.py
    └── database
        └── __init__.py # DB helpers (healthcheck) is here
```