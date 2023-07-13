from flask import Blueprint, request, render_template
from common.pagination import Pagination
from db import get_info

bp = Blueprint('items', __name__)

@bp.route('/items/')
def items():
    page = request.args.get('page', default=1, type=int)
    search_type = request.args.get('type', default="", type=str)
    items = get_info('item')

    data = []
    page_data = []

    # 아이템 타입 분류
    item_type = { item['Type'] for item in items }
    
    for item in items:
        if search_type in item['Type']:
            data.append(item)

    keywords = ""
    keywords += "&type=" + search_type

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("items.html", items = page_data, total_pages = total_pages, current_page = page, item_type = item_type, keywords=keywords)