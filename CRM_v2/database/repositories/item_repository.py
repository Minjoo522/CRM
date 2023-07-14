from database.repositories.common.datafetcher import DataFetcher

class Item(DataFetcher):
    def __init__(self):
        super().__init__()

    def get_search_data(self, search_type, page):
        query = f"Type LIKE ?"
        row = (f'%{search_type}%', )
        return self.get_page_item('item', page, query, row)
    
    def get_search_total_pages(self, search_type):
        query = f"Type LIKE ?"
        row = (f'%{search_type}%', )
        return self.get_total_pages('item', query, row)
    
    def get_type(self):
        return self.get_distinct('item', 'Type')