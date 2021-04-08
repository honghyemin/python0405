
# DemoDB4.py
import sqlite3

# 연결 객체 리턴
con = sqlite3.connect("c:\\work2\\Demo10.db")
# 커서 객체 리턴
cur = con.cursor()
cur.execute("select * from Emp;") # 조건 없이 몽땅 가져옴
for row in cur:
    print(row)