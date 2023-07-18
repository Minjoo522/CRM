from flask import Blueprint, render_template
from database.repositories.item_repository import Item

bp = Blueprint('item_detail', __name__)

@bp.route('/item_detail/<selected_id>/')
def item_detail(selected_id):
    db = Item()
    item = db.search_by_id('item', selected_id)
    month_revenues = db.get_month_revenue(selected_id)

    labels = []
    total_revenues = []
    for month_revenue in month_revenues:
        labels.append(month_revenue['month'])
        total_revenues.append(month_revenue['totalrevenue'])

    return render_template("item_detail.html", item = item, month_revenues = month_revenues, labels = labels, total_revenues = total_revenues)