import sqlite3

# 싱글톤?
class DbController:
    # 딕셔너리로 받아옴 - 변수 이름 변경 필요
    conn = sqlite3.connect('database/crm.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 튜플로 받아옴 - 변수 이름 변경 필요
    conn2 = sqlite3.connect('database/crm.db', check_same_thread=False)
    cursor2 = conn2.cursor()

    # user, item, store 디테일에 사용 가능!
    def searh_by_id(self, data_type, id):
        self.cursor.execute('select * from {} where id="{}"'.format(data_type, id))
        result = self.cursor.fetchone()
        return result

# DB 클래스 : conn, cursor -> 싱글톤?
# JOIN해야 하는 것
# 검색창 검색!

# order id / orderitem id / item
# SELECT OI.*, I.Name FROM orderitem OI
# JOIN orders O ON O.Id = OI.OrderId
# JOIN item I ON OI.ItemId = I.Id
# WHERE O.Id = "5d7b799e-d7fa-4267-b334-fc2d16a5373b";
