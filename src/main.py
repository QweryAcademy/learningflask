import os
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from .models import db
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired
# from wtforms.widgets import TextArea

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
database = os.path.join(BASE_DIR, "database.db")
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(database)
# app.config["SECRET_KEY"] = "hello"

db.init_app(app)
migrate = Migrate(app, db)

# class SearchResultForm(FlaskForm):
#     title = StringField("The title of the page", validators=[DataRequired()])
#     url = StringField("The url of the page", validators=[DataRequired()])
#     summary = StringField("Search Summary", widget=TextArea(), validators=[DataRequired()])
#
#     def save(self):
#         SearchResult.create(title=self.data['title'], url=self.data['url'], summary=self.data['summary'])
#
def create_tables():
    db.create_all(app)

from .views import *
