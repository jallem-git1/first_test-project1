import sqlite3

conn = sqlite3.connect('test.db')

'''cur = conn.cursor()
cur.execute("select * from student")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()'''

with conn:
    cur = conn.cursor()
    sql = "select * from student where id = ? or name = ?"
    cur.execute(sql, (1, '김상순'))
    rows = cur.fetchall()
    for row in rows:
        print(row)
