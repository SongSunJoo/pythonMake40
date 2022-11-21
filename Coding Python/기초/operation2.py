# 논리연산
# or, and, not
# True, False는 bool형
# or : 값이 하나라도 참일 경우에 참인 연산
print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 1)
print(False or False)
print(False or True)
print(True or False)
print(True or True)

# and : 모든 값이 참이어야 참인 연산
print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)
print(False and False)
print(False and True)
print(True and False)
print(True and True)

# not : 자신의 상태를 반전
# True -> False, False -> True
# not은 True 아니면 False의 두 가지 상태만은 가짐
# 숫자 타입도 bool형으로 노출
print(not 0)
print(not 1)
print(not False)
print(not True)