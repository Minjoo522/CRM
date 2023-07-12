import sqlite3

conn = sqlite3.connect('database/crm.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM user LIMIT 10')
result = cursor.fetchall()

print(result)