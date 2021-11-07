from werkzeug.utils import redirect
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    cards = [
        {
            'name': 'Black Lotus',
            'body': 'tap and sac to add 3 mana'
        },  
        {
            'name': 'Phyrexian Altar',
            'body': 'sac a creature to add 1 colored mana'
        }]
    return render_template('index.html', title="title", user=user, cards=cards)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}') # Posible error here...
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)