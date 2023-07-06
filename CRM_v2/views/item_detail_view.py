from flask import Blueprint, render_template
from load_file import load_file

bp = Blueprint('item_detail', __name__)

@bp.route('/item_detail/<selected_id>/')
def item_detail(selected_id):
    items = load_file("src/item.csv")
    for item in items:
        if item['Id'] == selected_id:
            return render_template("item_detail.html", item = item)