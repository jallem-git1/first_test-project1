import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정내가만일모든것을좋아한다면우리에겐무엇이더필요할까")
tel_nos=list("0123456789"*3)

def make_name():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))
    tel1 = "010"
    tel2 = "-"+"".join(random.sample(tel_nos, 4))
    tel3 = "-"+"".join(random.sample(tel_nos, 4))

    print(type(sung), type(name))
    #return sung + name
    #return (sung + name)
    return (sung + name, tel1+tel2+tel3) #튜플형태
   

#print(make_name())

data = []
for i in range(0,100):
    data.append(make_name())

print(data)
print("4444444444444444")
exit()

conn = sqlite3.connect('/Users/jakehong/sqlite/test.db')

'''cur = conn.cursor()
cur.execute("select * from student")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()'''

"""  이름과 전화번호를 튜플로 묶은 리스트를 만들어 일괄로 DB에 writing"""
"""
# exit()
conn = sqlite3.connect('/Users/jakehong/sqlite/test.db')

# 데이타 insert를 합니다.
with conn:
    cur = conn.cursor()
    sql = "insert into students(name, tel) values(?, ?)"
    cur.executemany(sql, data)
    conn.commit()

"""

with conn:
    cur = conn.cursor()
    sql = "select * from students"
    #sql = "select * from student where id = ? or name = ?"

    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
