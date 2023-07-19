from flask import Blueprint, request, redirect, url_for, render_template

# db
from database.repositories.item_repository import Item

bp = Blueprint('new_order', __name__)

@bp.route('/new_order/')
def new_order():
    nonuser_uuid = request.args.get('nonuser_uuid', type=str)
    # if nonuser_uuid:
        # nonuser면 index에서 받아온 uuid 리스트에 저장해놓고 계산하기 누르면 insert 되게
    item_db = Item()
    items = item_db.get_distinct('item', '*')
    return render_template('kiosk/new_order.html', items = items)