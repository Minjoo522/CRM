from flask import Blueprint, request, render_template
from database.repositories.store_repository import StoreDb

from model.models import Store

bp = Blueprint('stores', __name__)

@bp.route('/stores/')
def stores():
    db = StoreDb()

    page = request.args.get('page', default=1, type=int)
    search_store_name = request.args.get('store-name', default="", type=str)
    user_uuid = request.args.get('user_uuid')

    keywords = ""
    keywords += "&store-name=" + search_store_name

    if search_store_name:
        page_data, total_pages = db.get_search_result('store', page, search_store_name)
    else:
        total_pages = db.get_total_pages('store')
        page_data = db.get_page_item('store', page)

    addresses = db.get_addresses()
    cities = []
    for address in addresses:
        full_address = address['Address'].split()
        # 구 정보만 split
        cities.append(full_address[1])

    return render_template("stores.html", stores = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_store_name = search_store_name, user_uuid = user_uuid, cities = cities)