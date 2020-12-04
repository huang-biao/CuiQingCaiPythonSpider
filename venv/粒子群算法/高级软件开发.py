import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
# 创建表
# c.execute('''CREATE TABLE stocks(date text,trans text,symbol text,qty real,price real)''')
c.execute('''INSERT INTO stocks VALUES('2016-01-05','BUY','RHAT',100,35.14)''')
conn.commit()
# conn.close()
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

print(__file__)
print(__name__)