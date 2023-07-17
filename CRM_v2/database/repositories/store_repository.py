from database.repositories.common.datafetcher import DataFetcher

class Store(DataFetcher):
    def __init__(self):
        super().__init__()

    def build_query(self, search_name):
        query = f"Name LIKE ?"
        row = [f'%{search_name}%']
        return query, row