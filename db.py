import sqlite3

conn = sqlite3.connect('plushi.db')
cursor = conn.cursor()

sql_query = '''CREATE TABLE IF NOT EXISTS plushi(
    plush_id INTEGER PRIMARY KEY,
    animal TEXT,
    accessories TEXT,
    size TEXT
)'''

cursor.execute(sql_query)
conn.commit()
conn.close()
