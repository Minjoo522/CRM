from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    birthdate = db.Column(db.String(32))
    age = db.Column(db.Integer())
    address = db.Column(db.String(64))
    loginid = db.Column(db.String(64))
    loginpassword = db.Column(db.String(64))

class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(16))
    address = db.Column(db.String(64))

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String(64), primary_key = True)
    orderat = db.Column(db.String(32))
    storeid = db.Column(db.String(64))
    userid = db.Column(db.String(64))