import pymysql

conn=pymysql.connect(host='localhost',
user='root',password='qwer1234',db='test')

c=conn.cursor()
sql='''
    create table if not exists stocks
    (date text,trans text,symbol text, qty real, price real)
'''

c.execute(sql)
sql="insert into stocks values('2006-01-05','buy','rhat',100,35.14)"
c.execute(sql)
conn.commit()

conn.close()