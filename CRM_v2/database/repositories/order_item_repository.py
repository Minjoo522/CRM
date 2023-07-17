from database.repositories.common.datafetcher import DataFetcher

class OrderItem(DataFetcher):
    def __init__(self):
        super().__init__()

    def build_query(self, id):
        self.connect_to_row()
        query = f"""
                SELECT OI.*, I.Name FROM orderitem OI
                JOIN orders O ON O.Id = OI.OrderId
                JOIN item I ON OI.ItemId = I.Id
                WHERE O.Id = "{id}";
                """
        self.execute_query(query)
        result = self.fetch_one()
        self.close_connection
        return result