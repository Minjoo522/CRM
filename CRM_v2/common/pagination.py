class Pagination:
    PER_PAGE = 10

    # db: 쿼리문으로 한 번에 실행
    def get_total_pages(self, data):
        total_pages = len(data) // self.PER_PAGE + (len(data) % self.PER_PAGE > 0)
        return total_pages

    def get_start_index(self, page):
        start_index = self.PER_PAGE * (page - 1)
        return start_index

    def get_end_index(self, start_index):
        end_index = start_index + self.PER_PAGE
        return end_index