# IMPORTS
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

# FLASK ROUTES
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('index.html', title = "The Film Bucket Challenge", form = form)