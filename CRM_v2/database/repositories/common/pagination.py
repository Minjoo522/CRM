from database.controllers.db_controller import DbController

class Pagination(DbController):
    __PER_PAGE = 10
    def __init__(self):
        super().__init__

    def get_page_item(self, data_type, page):
        self.connect_to_row()
        query = f"SELECT * FROM {data_type} LIMIT ? OFFSET ?"
        offset = (page - 1) * self.__PER_PAGE
        self.execute_query(query, (self.__PER_PAGE, offset))
        result = self.fetch_all()
        return result

    def get_total_pages(self, data_type):
        self.connect()
        query = f"SELECT COUNT(*) FROM {data_type}"
        self.execute_query(query)
        count = self.fetch_one()[0]
        result = int(count) // self.__PER_PAGE + (int(count) % self.__PER_PAGE > 0)
        self.close_connection()
        return result
    