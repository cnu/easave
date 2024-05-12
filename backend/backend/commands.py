# -*- coding: utf-8 -*-
"""Click commands."""
import logging
import os

import click
from flask import Flask
from flask.cli import with_appcontext

from backend.extensions import db
from backend.models import User, Business, Deposit, Loan

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# @click.command()
@app.cli.command("create-db")
@with_appcontext
def create_db():
    """creates db tables - import your models within commands.py to create the models."""
    db.create_all()
    print("Database structure created successfully")


@click.command()
def clean():
    """Remove *.pyc and *.pyo files recursively starting at current directory.
    Borrowed from Flask-Script, converted to use Click.
    """
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith(".pyc") or filename.endswith(".pyo"):
                full_pathname = os.path.join(dirpath, filename)
                click.echo("Removing {}".format(full_pathname))
                os.remove(full_pathname)
