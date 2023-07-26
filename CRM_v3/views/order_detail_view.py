from flask import Blueprint, render_template
from database.repositories.orders_repository import OrderDb

bp = Blueprint('order_detail', __name__)

@bp.route('/order_detail/<selected_id>/')
def user_detail(selected_id):
    db = OrderDb()
    order = db.search_by_id('orders', selected_id)
    
    return render_template("order_detail.html", order = order)