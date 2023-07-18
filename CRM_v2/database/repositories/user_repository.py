from database.repositories.common.datafetcher import DataFetcher

class User(DataFetcher):
    def __init__(self):
        super().__init__()

    def build_query(self, search_name, search_gender):
        query = []
        row = []
        if search_name:
            query.append(f"Name LIKE ?")
            row.append(f'%{search_name}%')
        if search_gender:
            query.append(f"Gender LIKE ?")
            row.append(f'{search_gender}')
        query = " AND ".join(query)
        return query, row
    
    def user_orders(self, id):
        query = f"""
                SELECT Id, OrderAt, StoreId FROM orders
                WHERE UserId = '{id}'
                """
        return self.fetch_multiple_data(query)
    
    def find_top_visited_stores(self, id):
        query = f"""
                SELECT S.Name, COUNT(*) AS "visitcount"
                FROM store S JOIN orders O
                ON S.Id = O.StoreId
                WHERE O.UserId = "{id}"
                GROUP BY S.Name
                ORDER BY visitcount DESC
                LIMIT 5
                """
        return self.fetch_multiple_data(query)
    

    def find_top_ordered_items(self, id):
        query = f"""
                SELECT I.Name, COUNT(*) AS "ordercount"
                FROM item I JOIN orderitem OI
                ON I.Id = OI.ItemId
                JOIN orders O
                ON O.Id = OI.OrderId
                WHERE O.UserId = "{id}"
                GROUP BY I.Name
                ORDER BY ordercount DESC
                LIMIT 5
                """
        return self.fetch_multiple_data(query)