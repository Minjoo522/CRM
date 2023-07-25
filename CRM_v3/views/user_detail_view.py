from flask import Blueprint, render_template
from database.repositories.user_repository import User

bp = Blueprint('user_detail', __name__)

@bp.route('/user_detail/<selected_id>/')
def user_detail(selected_id):
    db = User()
    user = db.search_by_id('user', selected_id)
    user_orders = db.user_orders(selected_id)
    top_visited_stores = db.find_top_visited_stores(selected_id)
    top_ordered_items = db.find_top_ordered_items(selected_id)
    return render_template("user_detail.html", user = user, user_orders = user_orders, top_visited_stores = top_visited_stores, top_ordered_items = top_ordered_items)