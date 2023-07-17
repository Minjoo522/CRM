from database.repositories.common.datafetcher import DataFetcher

class User(DataFetcher):
    def __init__(self):
        super().__init__()

    def get_search_data(self, data_type, search_name, search_gender, page):
        query = []
        if search_name:
            query.append(f"Name LIKE '%{search_name}%'")
        if search_gender:
            query.append(f"Gender LIKE '{search_gender}%'")
        if query:
            query = " AND ".join(query)
        return self.get_page_item(data_type, page, query)
    
    def get_search_total_pages(self, data_type, search_name, search_gender):
        query = f"Name LIKE ? AND Gender LIKE ?"
        row = (f'%{search_name}%', search_gender)
        return self.get_total_pages(data_type, query, row)

