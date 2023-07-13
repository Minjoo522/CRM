from flask import Blueprint, request, render_template
from common.pagination import Pagination
from db import get_info

bp = Blueprint('stores', __name__)

@bp.route('/stores/')
def stores():
    page = request.args.get('page', default=1, type=int)
    search_store_name = request.args.get('store-name', default="", type=str)
    stores = get_info('store')

    data = []
    page_data = []

    for store in stores:
        if search_store_name.strip() in store['Name'][:-2]:
            data.append(store)

    keywords = ""
    keywords += "&store-name=" + search_store_name

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("stores.html", stores = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_store_name = search_store_name)