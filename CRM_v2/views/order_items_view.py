from flask import Blueprint, request, render_template
from common.pagination import Pagination
from db import get_info

bp = Blueprint('order_items', __name__)

@bp.route('/order_items/')
def order_items():
    page = request.args.get('page', default=1, type=int)
    order_items = get_info('orderitem')

    data = []
    page_data = []
    
    for order_item in order_items:
        data.append(order_item)

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("order_items.html", order_items = page_data, total_pages = total_pages, current_page = page)