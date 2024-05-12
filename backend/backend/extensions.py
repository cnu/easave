# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""
from flask_sqlalchemy import SQLAlchemy
from flask_firebase_admin import FirebaseAdmin

db = SQLAlchemy()
firebase = FirebaseAdmin()
