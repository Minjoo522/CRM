import sqlite3

conn = sqlite3.connect('database/crm.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
per_page = 10

# 싱글톤?
class DbController:
    # 딕셔너리로 받아옴
    conn = sqlite3.connect('database/crm.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 튜플로 받아옴
    conn2 = sqlite3.connect('database/crm.db', check_same_thread=False)
    cursor2 = conn2.cursor()

    def get_info(self, data_type):
        self.cursor.execute('select * from {}'.format(data_type))
        result = self.cursor.fetchall()
        return result
    
    def get_count(self, data_type):
        self.cursor2.execute('select count(*) from {}'.format(data_type))
        result = self.cursor2.fetchone()
        return int(result[0])
    
    def page_item(self, data_type, page):
        self.cursor.execute('select * from {} limit {} offset ({}-1)*{}'.format(data_type, per_page, page, per_page))
        result = self.cursor.fetchall()
        return result

    def searh_id(self, data_type, id):
        self.cursor.execute('select * from {} where id="{}"'.format(data_type, id))
        result = self.cursor.fetchone()
        return result

def get_info(data_type):
    cursor.execute('select * from {}'.format(data_type))
    results = cursor.fetchall()
    return results

# DB 클래스 : conn, cursor -> 싱글톤?
# JOIN해야 하는 것
# 검색창 검색!