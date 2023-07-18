from database.controllers.db_controller import DbController

class DataFetcher(DbController):
    __PER_PAGE = 10
    def __init__(self):
        super().__init__()

    def fetch_multiple_data(self, query):
        self.connect_to_row()
        query = query
        self.execute_query(query)
        result = self.fetch_all()
        self.close_connection()
        return result
    
    def search_by_id(self, data_type, id):
        self.connect_to_row()
        query = f"SELECT * FROM {data_type} WHERE Id=?"
        self.execute_query(query, (id, ))
        result = self.fetch_one()
        self.close_connection()
        return result

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
    
    def get_distinct(self, data_type, column):
        self.connect()
        query = f"SELECT DISTINCT {column} FROM {data_type}"
        self.execute_query(query)
        result = self.fetch_all()
        self.close_connection()
        return result

    def get_search_result(self, data_type, page, *args):
        query, row = self.build_query(*args)
        search_data = self.get_page_item(data_type, page, query, row)
        total_pages = self.get_total_pages(data_type, query, row)
        return search_data, total_pages