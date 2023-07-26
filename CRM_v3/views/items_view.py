from flask import Blueprint, request, render_template
from database.repositories.item_repository import ItemDb

from models import Item


bp = Blueprint('items', __name__)

@bp.route('/items/')
def items():
    db = ItemDb()

    page = request.args.get('page', default=1, type=int)
    search_type = request.args.get('type', default="", type=str)

    keywords = "&type=" + search_type

    item_type = db.get_type()

    if search_type:
        page_data, total_pages = db.get_search_result('item', page, search_type)
    else:
        total_pages = db.get_total_pages('item')
        page_data = db.get_page_item('item', page)

    return render_template("items.html", items = page_data, total_pages = total_pages, current_page = page, item_type = item_type, keywords=keywords)