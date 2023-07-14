from flask import Blueprint, request, render_template
from database.repositories.order_item_repository import OrderItem


bp = Blueprint('order_items', __name__)

@bp.route('/order_items/')
def order_items():
    db = OrderItem()

    page = request.args.get('page', default=1, type=int)

    total_pages = db.get_total_pages('orderitem')
    page_data = db.get_page_item('orderitem', page)

    return render_template("order_items.html", order_items = page_data, total_pages = total_pages, current_page = page)