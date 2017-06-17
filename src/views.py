<<<<<<< Updated upstream
from flask import request, redirect, render_template
from .main import app
=======
from flask import (
    render_template, flash,jsonify,
    request, redirect, session, url_for)
from .main import app, login_manager
>>>>>>> Stashed changes
from . import models

from flask_login import login_required, logout_user


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)


@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


value = 0


@app.route('/search')
@app.route('/results.html')
def search():
<<<<<<< Updated upstream
    site = request.args.get('site','')
    data = models.SearchResult.search(site)    
    return render_template('results.html', results = data, search_input=site)
=======
    site = request.args.get('site', '')
    data = models.SearchResult.search(site)
    return render_template('results.html', results=data, search_input=site)

>>>>>>> Stashed changes

@app.route('/admin', methods=['POST', 'GET'])
@login_required
def admin_view():
    form = SearchResultForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('/')
    return render_template('admin.html', form=form)
<<<<<<< Updated upstream
=======


@app.route("/login/", methods=['POST', 'GET'])
def login():
    login_form = forms.LoginForm()
    if login_form.validate_on_submit():
        login_form.login_user()
        flash('Logged in successfully.', "success")
        next_ = request.args.get('next')

        return redirect(next_ or url_for('home'))
    return render_template('login.html', form=login_form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.", "info")
    return redirect(url_for('home'))


@app.route("/all-users")
def all_users():
    users = models.User.query.all()
    return jsonify([dict(email=x.email, id=x.id) for x in users])
>>>>>>> Stashed changes
