from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash # I'll remove this and replace with a hashing function soon...

    def __repr__(self):
        return f'<User {self.email}>'

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True, nullable=False)
    released_at = db.Column(db.Date())
    image_url = db.Column(db.String(120))  # use Normal in off the API
    mana_cost = db.Column(db.String(40))
    cmc = db.Column(db.Integer)