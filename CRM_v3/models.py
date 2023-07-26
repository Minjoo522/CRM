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
    
    orderR = db.relationship('Orders', backref='user')

class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(16))
    address = db.Column(db.String(64))

    orderR = db.relationship('Orders', backref='store')

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String(64), primary_key = True)
    orderat = db.Column(db.String(32))
    storeid = db.Column(db.String(64), db.ForeignKey('store.id'))
    userid = db.Column(db.String(64), db.ForeignKey('user.id'))

    orderitemR = db.relationship('OrderItem', backref='orders')

class OrderItem(db.Model):
    __tablename__ = 'orderitem'
    id = db.Column(db.String(64), primary_key = True)
    orderid = db.Column(db.String(64), db.ForeignKey('orders.id'))
    itemid = db.Column(db.String(64), db.ForeignKey('item.id'))
    
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    unitprice = db.Column(db.Integer())

    orderitemR = db.relationship('OrderItem', backref='item')

class Admin(db.Model):
    __tablename__ = 'admin'
    loginid = db.Column(db.String(64), primary_key = True)
    loginpassword = db.Column(db.String(64))