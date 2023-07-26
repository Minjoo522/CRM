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

class OrderItem(db.Model):
    __tablename__ = 'orderitem'
    id = db.Column(db.String(64), primary_key = True)
    orderid = db.Column(db.String(64))
    
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    unitprice = db.Column(db.Integer())

class Admin(db.Model):
    __tablename__ = 'admin'
    loginid = db.Column(db.String(64), primary_key = True)
    loginpassword = db.Column(db.String(64))