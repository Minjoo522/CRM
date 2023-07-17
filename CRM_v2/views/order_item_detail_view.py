from flask import Blueprint, render_template
from database.repositories.order_item_repository import OrderItem

bp = Blueprint('order_item_detail', __name__)

@bp.route('/order_item_detail/<selected_id>/')
def order_item_detail(selected_id):
    db = OrderItem()
    order_item = db.build_query(selected_id)
    return render_template("order_item_detail.html", order_item = order_item)