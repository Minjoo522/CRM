from database.repositories.common.datafetcher import DataFetcher

class Item(DataFetcher):
    def __init__(self):
        super().__init__()

    def build_query(self, search_type):
        query = f"Type LIKE ?"
        row = [f'{search_type}']
        return query, row

    def get_type(self):
        return self.get_distinct('item', 'Type')
    
    def get_month_revenue(self, id):
        query = f"""
                SELECT SUBSTR(O.OrderAt, 1, 7) AS "month",
                sum(I.UnitPrice) AS "totalrevenue",
                COUNT(OI.Id) AS "itemcount"
                FROM item I JOIN orderitem OI
                ON I.Id = OI.ItemId
                JOIN orders O
                ON O.Id = OI.OrderID
                WHERE I.Id = "{id}"
                GROUP BY month;
                """
        return self.fetch_multiple_data(query)