from app import db

class UserDb(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    birthdate = db.Column(db.String(32))
    age = db.Column(db.Integer())
    address = db.Column(db.String(64))
    loginid = db.Column(db.String(64))
    loginpassword = db.Column(db.String(64))