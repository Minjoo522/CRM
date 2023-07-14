from database.repositories.common.datafetcher import DataFetcher

class User(DataFetcher):
    def __init__(self):
        super().__init__()

    def get_search_data(self, data_type, search_name, search_gender, page):
        query = f"Name LIKE ? AND Gender LIKE ?"
        row = (f'%{search_name}%', f'%{search_gender}%')
        return self.get_page_item(data_type, page, query, row)
    
    def get_search_total_pages(self, data_type, search_name, search_gender):
        query = f"Name LIKE ? AND Gender LIKE ?"
        row = (f'%{search_name}%', f'%{search_gender}%')
        return self.get_total_pages(data_type, query, row)

