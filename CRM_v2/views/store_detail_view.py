from flask import Blueprint, render_template
from common.load_file import load_file

bp = Blueprint('store_detail', __name__)

@bp.route('/store_detail/<selected_id>/')
def store_detail(selected_id):
    stores = load_file("src/store.csv")
    for store in stores:
        if store['Id'] == selected_id:
            return render_template("store_detail.html", store = store)