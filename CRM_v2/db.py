import sqlite3

conn = sqlite3.connect('database/crm.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

def get_info():
    cursor.execute('select * from user')
    results = cursor.fetchall()
    return results