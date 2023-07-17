import os
from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24)

# views
from views import items_view, login_view, logout_view,\
                    signup_view, users_view, user_detail_view, stores_view,\
                    store_detail_view, item_detail_view, orders_view, order_detail_view,order_items_view,\
                    order_item_detail_view, index_view

app.register_blueprint(login_view.bp)
app.register_blueprint(logout_view.bp)
app.register_blueprint(signup_view.bp)
app.register_blueprint(users_view.bp)
app.register_blueprint(user_detail_view.bp)
app.register_blueprint(stores_view.bp)
app.register_blueprint(store_detail_view.bp)
app.register_blueprint(items_view.bp)
app.register_blueprint(item_detail_view.bp)
app.register_blueprint(orders_view.bp)
app.register_blueprint(order_detail_view.bp)
app.register_blueprint(order_items_view.bp)
app.register_blueprint(order_item_detail_view.bp)
app.register_blueprint(index_view.bp)

if __name__ == "__main__":
    app.run(debug=True, port="8001")