from database.repositories.common.datafetcher import DataFetcher

class NewOrder(DataFetcher):
    def __init__(self):
        super().__init__()

    def insert_orders_data(self, uuid, order_at, store_id, user_id):
        query = "INSERT INTO orders VALUES (?, ?, ?, ?)"
        row = (uuid, order_at, store_id, user_id)
        return self.insert_data(query, row)

    def insert_orderitem_data(self, uuid, order_id, item_id):
        query = "INSERT INTO orderitem VALUES (?, ?, ?)"
        row = (uuid, order_id, item_id)
        return self.insert_data(query, row)