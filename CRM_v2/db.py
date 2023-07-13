import sqlite3

# TODO: 나중에 지우기
conn = sqlite3.connect('database/crm.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# TODO: 한 페이지 당 표시할 아이템 개수 어디에 정의할지 고민!
per_page = 10

# 싱글톤?
class DbController:
    # 딕셔너리로 받아옴 - 변수 이름 변경 필요
    conn = sqlite3.connect('database/crm.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 튜플로 받아옴 - 변수 이름 변경 필요
    conn2 = sqlite3.connect('database/crm.db', check_same_thread=False)
    cursor2 = conn2.cursor()

    def get_info(self, data_type):
        self.cursor.execute('select * from {}'.format(data_type))
        result = self.cursor.fetchall()
        return result
    
    def get_count(self, data_type):
        self.cursor2.execute('select count(*) from {}'.format(data_type))
        result = self.cursor2.fetchone()
        total_pages = int(result[0]) // per_page + (int(result[0]) % per_page > 0)
        return total_pages
    
    def page_item(self, data_type, page):
        self.cursor.execute('select * from {} limit {} offset ({}-1)*{}'.format(data_type, per_page, page, per_page))
        result = self.cursor.fetchall()
        return result

    def searh_id(self, data_type, id):
        self.cursor.execute('select * from {} where id="{}"'.format(data_type, id))
        result = self.cursor.fetchone()
        return result
    
    def search_name_gender(self, data_type, search_name, search_gender, page):
        self.cursor.execute(f'select * from {data_type} where name like "%{search_name}%" and gender like "%{search_gender}%" limit {per_page} offset ({page}-1)*{per_page}')
        result = self.cursor.fetchall()
        return result

    def search_total_page(self, data_type, search_name, search_gender):
        self.cursor2.execute(f'select count(*) from {data_type} where name like "%{search_name}%" and gender like "%{search_gender}%"')
        result = self.cursor2.fetchone()
        total_pages = int(result[0]) // per_page + (int(result[0]) % per_page > 0)
        return total_pages

# TODO: 나중에 삭제하기!
def get_info(data_type):
    cursor.execute('select * from {}'.format(data_type))
    results = cursor.fetchall()
    return results

# DB 클래스 : conn, cursor -> 싱글톤?
# JOIN해야 하는 것
# 검색창 검색!