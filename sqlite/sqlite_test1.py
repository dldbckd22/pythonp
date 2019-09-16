import sqlite3

conn = sqlite3.connect('D:/ai/pythonp/sqlite/example.db')
cursor = conn.cursor()
'''
symbol = input('심볼을 입력하세요(ex: RHAT).: ')
sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol
cursor.execute(sql)
print(cursor.fetchone())
conn.close()



symbol = input('심볼을 입력하세요(ex: RHAT).: ')
sql = 'SELECT * FROM stocks WHERE symbol=?'
symbol = (symbol,)
cursor.execute(sql, symbol)
print(cursor.fetchone())
conn.close()
'''

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00), 
            ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00), 
            ('2006-04-06', 'SELL', 'IBM', 500, 53.00), 
            ] 
cursor.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases) 
conn.commit()
           
cursor.execute('select * from stocks ORDER BY price') 
rows=cursor.fetchall() 
for row in rows: 
    print(row)

for row in cursor.execute('SELECT * FROM stocks ORDER BY price'): 
    print(row)
cursor.close()