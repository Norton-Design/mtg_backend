from datetime import datetime

from sqlalchemy.orm import relationship
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email):
        self.email = email
         # I'll remove this and replace with a hashing function soon...

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


# add more to this table as needed but start with the reserved list and slowly migrate the data as you go
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tcgplayer_id = db.Column(db.Integer)
    name = db.Column(db.String(40), index=True, nullable=False)
    released_at = db.Column(db.Date())
    image_url = db.Column(db.String(120))  # use Normal in off the API
    mana_cost = db.Column(db.String(40))
    cmc = db.Column(db.Integer)
    type_line = db.Column(db.String(40))
    oracle_text = db.Column(db.String(200)) # have to check to see if I need this to be longer...
    power = db.Column(db.String(2))
    toughness = db.Column(db.String(2))
    colors = db.Column(db.ARRAY(db.String))
    color_identity = db.Column(db.ARRAY(db.String), index=True)
    keywords = db.Column(db.ARRAY(db.String))
    reserved = db.Column(db.Boolean())
    reprint = db.Column(db.Boolean())
    set = db.Column(db.String(3))
    set_name = db.Column(db.String(40))
    set_type = db.Column(db.String(10))
    collector_number = db.Column(db.Integer)
    rarity = db.Column(db.String(8))
    artist = db.Column(db.String(20))
    edhrec_rank = db.Column(db.Integer)
    usd_price = db.Column(db.Float())
    comments = relationship('Comment', back_populates='card')
    
    def __init__(self, name, usd_price):
        self.name = name
        self.usd_price = usd_price
        # add more as needed...

    def __repr__(self):
        return f'<Card {self.name}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    card = relationship('Card', back_populates='comments')
    author = relationship('User')

class Watched_Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    starting_price = db.Column(db.Float())
    card = relationship('Card')
    user = relationship('User', back_populates='watched_cards')

class Owned_Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    starting_price = db.Column(db.Float())
    card = relationship('Card')
    user = relationship('User', back_populates='owned_cards')

class Combos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(256))
    approved = db.Column(db.Boolean())
    user = relationship('User', back_populates='combos')

class ComboPieces(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    combo_id = db.Column(db.Integer, db.ForeignKey('combo.id'))
    combo = relationship('Combo', back_populates='combo_pieces')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))