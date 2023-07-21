from flask import Blueprint, request, redirect, url_for, render_template

# db
from database.repositories.store_repository import Store

bp = Blueprint('select_store', __name__)

@bp.route('/select_store/')
def select_store():
    store_db = Store()
    selected_store = request.args.get('selected_store')
    selected_store_name = store_db.search_by_id('store', selected_store)
    stores = store_db.get_distinct('store', '*')

    return render_template('kiosk/select_store.html', stores = stores, selected_store_name = selected_store_name)