from flask import Blueprint, request, render_template

# db
from database.repositories.store_repository import Store

bp = Blueprint('select_store', __name__)

@bp.route('/select_store/<user_uuid>/')
def select_store(user_uuid):
    store_db = Store()
    selected_store = request.args.get('selected_store')
    selected_store_info = store_db.search_by_id('store', selected_store)
    stores = store_db.get_distinct('store', '*')
    user_uuid = user_uuid

    return render_template('kiosk/select_store.html', stores = stores, selected_store_info = selected_store_info, user_uuid = user_uuid)