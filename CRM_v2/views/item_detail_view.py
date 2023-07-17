from flask import Blueprint, render_template
from database.repositories.item_repository import Item

bp = Blueprint('item_detail', __name__)

@bp.route('/item_detail/<selected_id>/')
def item_detail(selected_id):
    db = Item()
    item = db.search_by_id('item', selected_id)
    return render_template("item_detail.html", item = item)