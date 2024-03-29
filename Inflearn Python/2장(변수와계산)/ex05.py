# 연산자의 간단한 실습
# 우선 순위가 제일 높은 것은 지수, (곱하기, 나누기, 나머지), (덧셈, 뺄셈) 순으로 정해지지만
# 우선 순위에 얽메이지 말고 괄호를 사용해서 가독성을 높이는 프로그램으로 작성을 하도록 하자.
# +, -, /, *은 오퍼레이터(연산자)
# 3, 4와 같은 것을 오퍼랜드(피연산자)라고 칭한다.

print(3 + 4)
print(3.14 * 5.0 * 5.0)
print(1 + (4 * 8) - (10 / 2))

# /를 하나만 적으면 실수 계산
print(10 / 3)

# //를  개로 적으면 정수 계산 - python에만 있음
print(10 // 3)

# 나머지 연산자
print(10 % 3)

# 지수(제곱)을 계산하려면 **연산자를 사용 - python에만 있음
print(3 ** 3)