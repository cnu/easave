# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

os_env = os.environ
load_dotenv()


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY", "3nF3Rn0")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    DATABASE_URL = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = (
        DATABASE_URL.replace("postgres://", "postgresql://")
        if DATABASE_URL
        else os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///easave.sqlite3")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", False)

    FIREBASE_API_KEY = "apiKey"
    FIREBASE_AUTH_DOMAIN = "projectId.firebaseapp.com"
