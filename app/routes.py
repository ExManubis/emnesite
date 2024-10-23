# IMPORTS
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from urllib.parse import urlsplit
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm
from app.models import User


# FLASK ROUTES

# GLOBAL ROUTES
@app.route('/login', methods=['GET', 'POST'])
def login():
    next_page = request.referrer
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = request.referrer
        return redirect(next_page)
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# ONBOARDING ROUTES
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template('index.html', title = "The Film Bucket Challenge", form = form)


@app.route('/welcome')
def welcome():
    form = LoginForm()
    return render_template('html/welcome.html', title = "Before You Begin", form = form)


# REEL 1 ROUTES
@app.route('/joan-of-arc')
def joan_of_arc():
    form = LoginForm()
    return render_template('html/reel_1/joan-of-arc.html', title = "Joan of Arc (1928)", form = form)


@app.route('/seven-samurai')
def seven_samurai():
    form = LoginForm()
    return render_template('html/reel_1/seven-samurai.html', title = 'Seven Samurai (1954)', form = form)


@app.route('/persona')
def persona():
    form = LoginForm()
    return render_template('html/reel_1/persona.html', title = 'Persona (1966)', form = form)


@app.route('/star-wars')
def star_wars():
    form = LoginForm()
    return render_template('html/reel_1/star-wars.html', title = 'Star Wars (1977)', form = form)


@app.route('/goodfellas')
def goodfellas():
    form = LoginForm()
    return render_template('html/reel_1/goodfellas.html', title = 'Goodfellas (1990)', form = form)


@app.route('/congrats_1')
def congrats_1():
    form = LoginForm()
    return render_template('html/reel_1/congrats.html', title = 'Congratulations!', form = form)


# REEL 2 ROUTES
@app.route('/godzilla')
def godzilla():
    form = LoginForm()
    return render_template('html/reel_2/godzilla.html', title = "Godzilla (1954)", form = form)


@app.route('/space-odyssey')
def space_odyssey():
    form = LoginForm()
    return render_template('html/reel_2/space-odyssey.html', title = "2001: A Space Odyssey (1968)", form = form)


@app.route('/godfather')
def godfather():
    form = LoginForm()
    return render_template('html/reel_2/godfather.html', title = "The Godfather (1972)", form = form)


@app.route('/stalker')
def stalker():
    form = LoginForm()
    return render_template('html/reel_2/stalker.html', title = "Stalker (1979)", form = form)


@app.route('/shoah')
def shoah():
    form = LoginForm()
    return render_template('html/reel_2/shoah.html', title = "Shoah (1986)", form = form)


@app.route('/congrats_2')
def congrats_2():
    form = LoginForm()
    return render_template('html/reel_2/congrats.html', title = "Congratulations!", form = form)