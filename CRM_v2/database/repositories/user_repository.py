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