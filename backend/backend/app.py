from flask import Flask, request, render_template


from backend import commands
from backend.extensions import db, firebase, cors
from backend.settings import Config as cfg
from backend import views


def create_app(config_object=cfg):
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route("/")
    def index():
        return {"page": "index"}

    @app.route("/health/")
    def health():
        return {"status": "OK"}

    register_blueprints(app)
    register_extensions(app)

    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    firebase.init_app(app)
    cors.init_app(app)


def register_blueprints(app):
    app.register_blueprint(views.bp)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.create_db)
