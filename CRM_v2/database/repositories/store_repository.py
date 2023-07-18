from database.repositories.common.datafetcher import DataFetcher

class Store(DataFetcher):
    def __init__(self):
        super().__init__()

    def build_query(self, search_name):
        query = f"Name LIKE ?"
        row = [f'%{search_name}%']
        return query, row
    
    def get_month_revenue(self, id):
        query = f"""
                    SELECT SUBSTR(O.OrderAt, 1, 7) AS "month",
                    sum(I.UnitPrice) AS "totalrevenue",
                    COUNT(OI.Id) AS "itemcount"
                    FROM item I, store S JOIN orderitem OI
                    ON I.Id = OI.ItemId
                    JOIN orders O
                    ON O.Id = OI.OrderID
                    WHERE S.Id = "{id}"
                    GROUP BY month
                """
        return self.fetch_multiple_data(query)