from flask_wtf import FlaskForm
from .models import SearchResult, User
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea, PasswordInput
from flask_login import login_user
from wtforms.validators import ValidationError


class SearchResultForm(FlaskForm):
    title = StringField("The title of the page", validators=[DataRequired()])
    url = StringField("The url of the page", validators=[DataRequired()])
    summary = StringField(
        "Search Summary", widget=TextArea(), validators=[DataRequired()])

    def save(self):
        SearchResult.create(
            title=self.data['title'], url=self.data['url'], summary=self.data['summary'])


class LoginForm(FlaskForm):
    email = StringField("Email or username", validators=[DataRequired()])
    password = StringField(
        "Password", widget=PasswordInput(), validators=[DataRequired()])

    def validate_email(self, field):
        if field.data  != "gbozee@example.com":
            self.email.errors.append("You are not a superuser")

    def login_user(self):
        email = self.data['email']
        password = self.data['password']
        new_user = User.query.filter(User.email==email).first()
        if new_user:
            result = login_user(new_user)

    def validate(self):
        rv = super().validate()
        if not rv:
            return False
        if not self._validate_credentials():
            self.email.errors.append('Invalid email/password combination')
            return False
        return True

    def _validate_credentials(self):
        if self.data.get('email') and self.data.get('password') == 'johndoe':
            return True
        return False
        # return self.data.get('email') and self.data.get('password') ==
        # 'johndoe':
