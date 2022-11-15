# range() 함수 실습하기

# 1. range(x) 매개변수 1개짜리 함수를 이용
hap = 0
for x in range(10):
    hap = hap + x
print("1. 0~9까지의 누계합 :", hap)

# 2. range(start, stop) 매개변수 2개짜리 함수를 이용
# 누적을 하는데 stop 값은 포함하지 않는다.
hap = 0
for x in range(0, 10):
    hap = hap + x
print("2. 0~9까지의 누계합 :", hap)