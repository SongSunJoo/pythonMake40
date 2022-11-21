# 조건문 : 조건에 따라 코드를 실행하거나 실행하지 않게 할 수 있음
# if 조건문 뒤에 :을 붙여줌
# 조건문을 만족하면 동작하는 코드는 조건문에 들여쓰기를 함 (Tab키)
# == 같을 때 참 / != 다를 때 참
a = 1
b = 1
if a == b:
    print("두 개의 값은 같습니다.")
if a != b:
    print("두 개의 값은 다릅니다.")
    
    
# if else : if 조건이 만족하지 않을 경우 else 사용
a = 1
b = 2
if a == b:
    print("두 개의 값은 같습니다.")
else:
    print("두 개의 값은 다릅니다.")
    
# if elif else : 여러 개의 조건을 비교할 수 있음
a = 1
b = 2
if a > b:
    print("a 값이 더 큽니다.")
elif a < b:
    print("b 값이 더 큽니다.")
else:
    print("두 개의 값은 같습니다.")
    
# >= 크거나 같을 때 참 / <= 작거나 같을 때 참
a = 1
b = 1
if a >= b:
    print("a 값이 더 크거나 같습니다.")
if a <= b:
    print("a 값이 더 작거나 같습니다.")
    
# 비교연산자인 and와 or를 이용한 비교문
a = 1
b = 1
c = 2
d = 2
if a == b and c == d:
    print("두 조건 모두 만족")
if a == b or c == d:
    print("두 조건 중 하나라도 만족하면")
    
# 조건문에서 문자열 비교
# == 비교 시 완전 같아야 참
# in으로 비교 시에 포함되어 있으면 참
# not in은 포함되어 있지 않으면 참
a_str = "hello python"
if a_str == "hello python":
    print("hello python 문자열이 같습니다.")
if a_str == "hi python":
    print("hi python 문자열이 같습니다.")
if "hello" in a_str:
    print("hello가 포함되어 있습니다.")
if "hi" in a_str:
    print("hi가 포함되어 있습니다.")
if "hi" not in a_str:
    print("hi가 포함되어 있지 않습니다.")
    
# in은 리스트의 요소값을 비교할 때도 사용
a_list = ["안녕", 1, 2, "python"]
if "안녕" in a_list:
    print("a_list에 안녕이 포함되어 있습니다.")
if "샴페인" in a_list:
    print("a_list에 샴페인이 포함되어 있습니다.")
if 2 in a_list:
    print("a_list에 2가 포함되어 있습니다.")
    
# not in도 리스트의 요소 비교를 위해 사용
if "안녕" not in a_list:
    print("a_list에 안녕이 포함되어 있지 않습니다.")
if 5 not in a_list:
    print("a_list에 5는 없습니다.")