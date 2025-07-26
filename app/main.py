from yaml import safe_load
from os import makedirs
from logging.config import dictConfig
from logging import getLogger
from flask import Flask
from utils.database import is_postgres_healthy


def load_config(path: str = "settings.yml") -> dict:
    makedirs("logs", exist_ok=True)
    with open(path, "r") as f:
        config = safe_load(f)
    dictConfig(config["logging"])
    return config


def create_app() -> Flask:
    app = Flask(__name__)
    config = load_config()
    app.config.update(config["flask"])
    logger = getLogger("app")
    logger.info("Flask application initialized successfully")
    logger.info(f"Flask settings: {app.config}")

    return app


if __name__ == "__main__":
    app = create_app()
    if not is_postgres_healthy(
        app.config["db_connection_string"]
    ):
        raise RuntimeError("PostgreSQL fail")
    
    app.run(
        host=app.config["host"],
        port=app.config["port"],
        debug=app.config["debug"]
    )
