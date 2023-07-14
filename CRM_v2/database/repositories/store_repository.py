from database.repositories.common.datafetcher import DataFetcher

class Store(DataFetcher):
    def __init__(self):
        super().__init__()

    def get_search_data(self, data_type, search_name, page):
        query = f"Name LIKE ?"
        row = (f'%{search_name}%', )
        return self.get_page_item(data_type, page, query, row)
    
    def get_search_total_pages(self, data_type, search_name):
        query = f"Name LIKE ?"
        row = (f'%{search_name}%', )
        return self.get_total_pages(data_type, query, row)