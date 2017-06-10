from flask import request, redirect, render_template
from .main import app
from . import models

@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/search')
@app.route('/results.html')
def search():
    site = request.args.get('site','')
    data = models.SearchResult.search(site)    
    return render_template('results.html', results = data, search_input=site)

@app.route('/admin', methods=['POST', 'GET'])
def admin_view():
    form = SearchResultForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('/')
    return render_template('admin.html', form=form)
