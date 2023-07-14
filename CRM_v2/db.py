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

    # 이동 완료!
    def get_total_pages(self, data_type):
        self.cursor2.execute('select count(*) from {}'.format(data_type))
        count = self.cursor2.fetchone()
        result = int(count[0]) // per_page + (int(count[0]) % per_page > 0)
        return result

    # 이동 완료!
    def page_item(self, data_type, page):
        self.cursor.execute('select * from {} limit {} offset ({}-1)*{}'.format(data_type, per_page, page, per_page))
        result = self.cursor.fetchall()
        return result

    # user, item, store 디테일에 사용 가능!
    def searh_by_id(self, data_type, id):
        self.cursor.execute('select * from {} where id="{}"'.format(data_type, id))
        result = self.cursor.fetchone()
        return result

    # 필요한 페이지 각각 만들어 주는게 좋을지?
    def search_name_gender(self, data_type, search_name, search_gender, page):
        query = f"SELECT * FROM {data_type} WHERE Name LIKE ? AND Gender LIKE ? LIMIT {per_page} OFFSET ({page}-1)*{per_page}"
        self.cursor.execute(query, (f"%{search_name}%", f"%{search_gender}%"))
        result = self.cursor.fetchall()
        return result

    def get_search_total_pages(self, data_type, search_name, search_gender):
        query = f"SELECT COUNT(*) FROM {data_type} WHERE Name LIKE ? AND Gender LIKE ?"
        self.cursor2.execute(query, (f"%{search_name}%", f"%{search_gender}%"))
        count = self.cursor2.fetchone()
        result = int(count[0]) // per_page + (int(count[0]) % per_page > 0)
        return result

# TODO: 나중에 삭제하기!
def get_info(data_type):
    cursor.execute('select * from {}'.format(data_type))
    results = cursor.fetchall()
    return results

# DB 클래스 : conn, cursor -> 싱글톤?
# JOIN해야 하는 것
# 검색창 검색!

# order id / orderitem id / item
# SELECT OI.*, I.Name FROM orderitem OI
# JOIN orders O ON O.Id = OI.OrderId
# JOIN item I ON OI.ItemId = I.Id
# WHERE O.Id = "5d7b799e-d7fa-4267-b334-fc2d16a5373b";
