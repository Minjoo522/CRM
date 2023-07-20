from flask import Blueprint, request, redirect, url_for, render_template

# db
from database.repositories.item_repository import Item

bp = Blueprint('new_order', __name__)

@bp.route('/new_order/')
def new_order():
    item_db = Item()
    items = item_db.get_distinct('item', '*')
    return render_template('kiosk/new_order.html', items = items)