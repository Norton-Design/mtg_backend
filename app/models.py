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
    
    def __init__(self, name, usd_price):
        self.name = name
        self.usd_price = usd_price
        # add more as needed...

    def __repr__(self):
        return f'<Card {self.name}>'
