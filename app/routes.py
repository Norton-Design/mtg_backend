from app import app
from flask import render_template

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