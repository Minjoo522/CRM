from flask import Blueprint, request, render_template
import uuid
from datetime import datetime

# db
from database.repositories.item_repository import Item
from database.repositories.new_order_repository import NewOrder

bp = Blueprint('new_order', __name__)

@bp.route('/new_order/<user_uuid>/<store_uuid>', methods=['GET', 'POST'])
def new_order(user_uuid, store_uuid):
    item_db = Item()
    new_order_db = NewOrder()
    items = item_db.get_distinct('item', '*')
    # try-except 고치기
    if request.method == 'POST':
        try: 
            ordered_items = request.get_json()

            order_uuid = str(uuid.uuid4())
            # TODO: 날짜 형식 확인
            order_at = datetime.now()
            store_id = store_uuid
            user_id = user_uuid
            new_order_db.insert_orders_data(order_uuid, order_at, store_id, user_id)

            for ordered_item in ordered_items:
                orderitem_uuid = str(uuid.uuid4())
                order_id = order_uuid
                item_id = ordered_item['Id']
                new_order_db.insert_orderitem_data(orderitem_uuid, order_id, item_id)
        except:
            pass
    
    return render_template('kiosk/new_order.html', items = items)