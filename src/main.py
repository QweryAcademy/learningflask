import os
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
<<<<<<< Updated upstream
from .models import db
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired
# from wtforms.widgets import TextArea
=======
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
>>>>>>> Stashed changes

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
database = os.path.join(BASE_DIR, "database.db")
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(database)
<<<<<<< Updated upstream
# app.config["SECRET_KEY"] = "hello"

db.init_app(app)
=======
app.config["SECRET_KEY"] = "hello"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

login_manager = LoginManager()
>>>>>>> Stashed changes
migrate = Migrate(app, db)
toolbar = DebugToolbarExtension(app)

<<<<<<< Updated upstream
# class SearchResultForm(FlaskForm):
#     title = StringField("The title of the page", validators=[DataRequired()])
#     url = StringField("The url of the page", validators=[DataRequired()])
#     summary = StringField("Search Summary", widget=TextArea(), validators=[DataRequired()])
#
#     def save(self):
#         SearchResult.create(title=self.data['title'], url=self.data['url'], summary=self.data['summary'])
#
=======
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"
    
>>>>>>> Stashed changes
def create_tables():
    db.create_all(app)

from .views import *
