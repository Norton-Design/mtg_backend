from flask_login.utils import login_required
from werkzeug.utils import redirect
from werkzeug.urls import url_parse
from app import app, db
from app.models import User
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
@login_required
def index():
    cards = [
        {
            'name': 'Black Lotus',
            'body': 'tap and sac to add 3 mana'
        },  
        {
            'name': 'Phyrexian Altar',
            'body': 'sac a creature to add 1 colored mana'
        }]
    return render_template('index.html', title="Home Page", cards=cards)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="Sign In", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    sample_posts = [
        {"author": user, 'body': "test post 1"},
        {"author": user, 'body': "test post 2"}
    ]
    # user = {'username': "sample shit", 'email': 'other shit'}
    return render_template('user.html', user=user, posts=sample_posts)


@app.route('/card/<string:name>')
def get_card(name):
    pass

@app.route('/card', methods=["POST"])
def create_card():
    pass

@app.route('/user/<string:username')
def get_user(username):
    pass

@app.route('/user', methods=['POST'])
def create_user():
    pass
