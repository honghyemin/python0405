# DemoRandom.py
# 임의의 숫자 만들기
import random

# 0.0 ~ 1.0
print( random.random())
print( random.random())
# 2.0 ~ 5.0
print( random.uniform(2.0, 5.0))

# 임의의 정수 만들기
print( [random.randrange(20) for i in range(10)])
print( [random.randrange(20) for i in range(10)])

# 유일한 값이 생성
print( random.sample(range(20), 10))
print( random.sample(range(20), 10))

print("-----------------------------")

# 로또 번호
lotto = list(range(1, 46))
print ( lotto )
random.shuffle(lotto)

for item in range(5):
    print(lotto.pop())
