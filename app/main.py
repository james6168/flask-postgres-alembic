from yaml import safe_load
from os import makedirs
from logging.config import dictConfig
from logging import getLogger
from flask import Flask, g, jsonify
from utils.database import is_postgres_healthy
from database import DatabaseConnection
from routes.auth import auth_bp
from pydantic import ValidationError



def load_config(path: str = "settings.yml") -> dict:
    makedirs("logs", exist_ok=True)
    with open(path, "r") as f:
        config = safe_load(f)
    dictConfig(config["logging"])
    return config


app = Flask(__name__)
config = load_config()
app.config.update(config["flask"])
db = DatabaseConnection(app.config["db_connection_string"])
logger = getLogger("app")
logger.info("Flask application initialized successfully")
logger.info(f"Flask settings: {app.config}")
app.register_blueprint(auth_bp)




@app.before_request
def create_db_session():
    g.db_session = db.connect()


@app.teardown_request
def close_db_session(exception=None):
    db.close()


@app.errorhandler(ValidationError)
def handle_pydantic_validation_error(e: ValidationError):
    return jsonify({
        "errors": e.errors(include_url=False, include_context=False)
    }), 400

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200



if __name__ == "__main__":
    if not is_postgres_healthy(
        app.config["db_connection_string"]
    ):
        raise RuntimeError("PostgreSQL fail")
    
    app.run(
        host=app.config["host"],
        port=app.config["port"],
        debug=app.config["debug"]
    )
