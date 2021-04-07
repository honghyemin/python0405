# DemoDB1.py

# SQLite를 사용하는 데모(로컬 데이터베이스)
import sqlite3

# 처음에는 데이터베이스파일 ( 또는 메모리 )를 생성
con = sqlite3.connect(":memory:")
# SQL구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()
# 저장소(테이블)을 만들기 : 테이블 스키마(뼈대)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
# 입력 파라메터 처리(python format {0}.{1})
# 텍스트박스(GUI, Web Page)에서 입력을 받아서 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber)) # (?,?) 입력받기위해서 여지를 남겨둠

# 다중의 레코드 ( 행, row )를 입력받는 경우 : 2차원 행렬데이터
datalist = (("tom", "010-123"),("dsp","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist) # datalist : 2차원이므로 한번에 집어넣음..?
 
# 검색
cur.execute("select * from PhoneBook;") # 모든 컬럼 !
for row in cur:
    print(row)