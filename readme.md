# Flask PostgreSQL Alembic Template Application

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