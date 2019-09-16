import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)


conn = sqlite3.connect('D:/ai/pythonp/sqlite/example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE if not exists stocks 
            (date text, trans text, symbol text, qty real, price real)''')
sql = ("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
cursor.execute(sql)
conn.commit()
conn.close()
