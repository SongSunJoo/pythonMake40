# while : 참과 거짓을 기준으로 조건이 거짓이 되기 전까지 무한 반복적으로 실행
# 조건이 참일 때 계속 반복
# 참인 조건 : True이거나 1 이상
a = 0
while a < 5:
    print(a)
    a = a + 1

# while True: 사용하여 동일한 동작 -> 계속 동작
# break 사용하여 탈출
a = 0
while True:
    print(a)
    a = a + 1
    if a >= 5:
        break
