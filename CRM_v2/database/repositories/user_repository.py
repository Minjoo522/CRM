from database.repositories.common.datafetcher import DataFetcher

class User(DataFetcher):
    def __init__(self):
        super().__init__()

    def get_search_result(self, data_type, search_name, search_gender, page):
        query = self.build_query(search_name, search_gender)
        search_data = self.get_page_item(data_type, page, query)
        total_pages = self.get_total_pages(data_type,query)
        return search_data, total_pages

    def build_query(self, search_name, search_gender):
        query = []
        if search_name:
            query.append(f"Name LIKE '%{search_name}%'")
        if search_gender:
            query.append(f"Gender LIKE '{search_gender}%'")
        query = " AND ".join(query)
        return query

