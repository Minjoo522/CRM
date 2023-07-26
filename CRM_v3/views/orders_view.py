from flask import Blueprint, request, render_template
from database.repositories.orders_repository import OrderDb

from models import Orders

bp = Blueprint('orders', __name__)

@bp.route('/orders/')
def orders():
    db = OrderDb()

    page = request.args.get('page', default=1, type=int)

    total_pages = db.get_total_pages('orders')
    page_data = db.get_page_item('orders', page)

    return render_template("orders.html", orders = page_data, total_pages = total_pages, current_page = page)