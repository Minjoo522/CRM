from models import *
from app import db
from repositories.data_repository import DataRepository

class UserRepository(DataRepository):
    def __init__(self):
        super().__init__()
    
    def user_orders(self, id):
        return db.session.query(Orders.id, Orders.orderat, Orders.storeid).filter_by(userid=id).all()