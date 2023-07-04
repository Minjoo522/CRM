from flask import Blueprint, render_template

bp = Blueprint('order_item_detail', __name__)

@bp.route('/order_item_detail')
def order_item_detail():
    return render_template("order_item_detail.html")