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