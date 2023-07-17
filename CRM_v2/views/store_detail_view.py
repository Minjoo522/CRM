from flask import Blueprint, render_template
from database.repositories.store_repository import Store

bp = Blueprint('store_detail', __name__)

@bp.route('/store_detail/<selected_id>/')
def store_detail(selected_id):
    db = Store()
    store = db.search_by_id('store', selected_id)
    return render_template("store_detail.html", store = store)