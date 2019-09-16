import pymysql

conn=pymysql.connect(host='localhost',
                    user='root',
                    password='qwer1234',
                    db='test',
                    cursorclass=pymysql.cursors.DictCursor)
c=conn.cursor()
symbol=input('심볼을 입력하세요')
sql="select * from stocks where symbol='%s'"%symbol
sql='select * from stocks where symbol=%s'
c.execute(sql,(symbol,))
print(c.fetchall())
