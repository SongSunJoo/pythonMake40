# 부울(bool) 변수 알아보기
# 부울 변수의 용도는 플래그 변수 형태로 사용을 많이 한다.
# 타 프로그래밍 언어에서는 부울변수의 값은 소문자로 시양하는 true, false를 사용하지만
# 파이썬은 대문자로 시작하는 True, False를 사용함을 잊지 않도록 한다.

flag = True
print(type(flag))
print(flag)

# 파이썬에서 부울 변수의 값을 바꾸기 위해서는 not 연산자를 이용하면 된다.
flag = not flag
print(type(flag))
print(flag)

if flag:
    print("참이라서 실행됩니다.")
else:
    print("거짓이라서 실행됩니다.")
    flag = not flag
    
if flag:
    print("참이라서 실행됩니다.")
else:
    print("거짓이라서 실행됩니다.")