from flask import Blueprint, request, render_template
from database.repositories.order_repository import Order


bp = Blueprint('orders', __name__)

@bp.route('/orders/')
def orders():
    db = Order()

    page = request.args.get('page', default=1, type=int)

    # if search_store_name:
    #     total_pages = db.get_search_total_pages('store', search_store_name)
    #     page_data = db.get_search_data('store', search_store_name, page)
    # else:
    total_pages = db.get_total_pages('orders')
    page_data = db.get_page_item('orders', page)

    return render_template("orders.html", orders = page_data, total_pages = total_pages, current_page = page)