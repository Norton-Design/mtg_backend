from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f'<User {self.email}>'