import pymysql
def conn_db():
    conn = pymysql.connect(host='localhost',
        user='root',
        password='qwer1234',
        db='test', 
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return conn

def create_table():
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute('''create table if not exists books(
        title text,
        published_date text,
        publisher text, pages integer,
        recommend integer
        )''')
    conn.commit()
    conn.close()
def insert_books(item):
    conn=conn_db()
    cursor=conn.cursor()
    sql='insert into books values(%s,%s,%s,%s,%s)' 
    
   
    cursor.execute(sql,item)
    conn.commit()
    conn.close()

def all_books(count=0):
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute("select * from books")
    if count==0:
        print('[1] 전체 데이터 출력하기')
        books=cursor.fetchall()
        print(books) 
        for book in books:
            for i in book:
                print(book[i],end=" ")
            print()
    else:
        books=cursor.fetchmany(count)
        print(books)
        for book in books:
            for i in book:
                print(book[i],end='')
            print()

    conn.close()

    
