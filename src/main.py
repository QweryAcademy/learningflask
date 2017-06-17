import os
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from .models import db
from flask_login import LoginManager
FLASK_CONFIGURATION = os.getenv("FLASK_CONFIGURATION", "settings/local.py")
if FLASK_CONFIGURATION == 'settings/local.py':
    from flask_debugtoolbar import DebugToolbarExtension


def create_app(config_file=FLASK_CONFIGURATION):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_pyfile(config_file)
    migrate = Migrate(app, db)
    if FLASK_CONFIGURATION == 'settings/local.py':
        toolbar = DebugToolbarExtension(app)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = "login"

    login_manager.init_app(app)
    with app.app_context():
        from src import views
        views.login_manager.init_app(app)

    return app


app = create_app()


def create_tables():
    db.create_all(app)
