from flask import Blueprint, request, render_template
from database.repositories.store_repository import Store

bp = Blueprint('stores', __name__)

@bp.route('/stores/')
def stores():
    db = Store()

    page = request.args.get('page', default=1, type=int)
    search_store_name = request.args.get('store-name', default="", type=str)

    keywords = ""
    keywords += "&store-name=" + search_store_name

    if search_store_name:
        page_data, total_pages = db.get_search_result('store', page, search_store_name)
    else:
        total_pages = db.get_total_pages('store')
        page_data = db.get_page_item('store', page)

    return render_template("stores.html", stores = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_store_name = search_store_name)