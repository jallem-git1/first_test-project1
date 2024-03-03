import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정내가만일모든것을좋아한다면우리에겐무엇이더필요할까")
tel_nos=list("0123456789"*5)

print(type(random.choices(fam_names)))

def make_name():
    sung = random.choice(fam_names)
      
    name = "".join(random.sample(first_names, 2))
    tel1 = "010"
    tel2 = "-"+"".join(random.sample(tel_nos, 4))
    tel3 = "-"+"".join(random.sample(tel_nos, 4))

    # print(type(sung), type(name))
    #return sung + name
    #return (sung + name)
    return (sung + name, tel1+tel2+tel3) #튜플형태
    

data = []
for i in range(0,20):
    data.append(make_name())

print(data)

# for i in data:
#     print(i)



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
