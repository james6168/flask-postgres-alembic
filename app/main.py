from yaml import safe_load
from os import makedirs
from logging.config import dictConfig
from flask import Flask

makedirs("logs", exist_ok=True)
    
with open("settings.yml", "r") as settings_file:
    config = safe_load(settings_file)

dictConfig(config["logging"])


def create_app() -> Flask:
    app = Flask(__name__)

    app.logger.info("Flask application initialized successfully")

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(
        host=config["flask"]["host"],
        port=config["flask"]["port"],
        debug=config["flask"]["debug"]
    )
