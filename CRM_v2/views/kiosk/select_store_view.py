from flask import Blueprint, request, redirect, url_for, render_template

# db
from database.repositories.store_repository import Store

bp = Blueprint('select_store', __name__)

@bp.route('/select_store/')
def select_store():
    nonuser_uuid = request.args.get('nonuser_uuid', type=str)
    # if nonuser_uuid:
        # nonuser면 index에서 받아온 uuid 리스트에 저장해놓고 계산하기 누르면 insert 되게
    store_db = Store()
    stores = store_db.get_distinct('store', '*')
    return render_template('kiosk/select_store.html', stores = stores)