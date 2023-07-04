from flask import Blueprint, request, render_template
from load_file import load_file
from pagination import Pagination

bp = Blueprint('orders', __name__)

@bp.route('/orders')
def orders():
    page = request.args.get('page', default=1, type=int)
    orders = load_file("src/order.csv")

    data = []
    page_data = []
    
    for order in orders:
        data.append(order)

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("orders.html", orders = page_data, total_pages = total_pages, current_page = page)