from database.controllers.db_controller import DbController

class DataFetcher(DbController):
    __PER_PAGE = 10
    def __init__(self):
        super().__init__()
    
    def get_page_item(self, data_type, page, search=None, row=None):
        self.connect_to_row()
        offset = (page - 1) * self.__PER_PAGE
        if search:
            query = f"SELECT * FROM {data_type} WHERE {search} LIMIT ? OFFSET ?"
            self.execute_query(query, (*row, self.__PER_PAGE, offset))
        else:
            query = f"SELECT * FROM {data_type} LIMIT ? OFFSET ?"
            self.execute_query(query, (self.__PER_PAGE, offset))
        result = self.fetch_all()
        self.close_connection()
        return result

    def get_total_pages(self, data_type, search=None, row=None):
        self.connect()
        if search:
            query = f"SELECT COUNT(*) FROM {data_type} WHERE {search}"
            self.execute_query(query, row)
        else:
            query = f"SELECT COUNT(*) FROM {data_type}"
            self.execute_query(query)
        count = int(self.fetch_one()[0])
        result = count // self.__PER_PAGE + (count % self.__PER_PAGE > 0)
        self.close_connection()
        return result
    