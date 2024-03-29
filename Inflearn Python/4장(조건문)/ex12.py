# 논리 연산자(logical operator)는 두 개 이상의 조건을 조합해서 
# 참인지 거짓인지를 계산할 때 사용하는 연산자이다.
# 논리 연산자의 종류에는 and(논리곱), or(논리합), not(논리부정)이 있다.

# and 논리 연산자의 실습
name = "송선주"
age = 14
height = 160

# and 논리 연산자는 여러 개의 조건 중에서 처음 조건이 거짓이라면
# 다른 조건은 전혀 검사 조차 하지 않는다. (단축 계산)
# and 논리 연산자는 모든 조건이 참이어야지만 참을 반환한다. (중요)
if age >= 14 and height >= 160 and name == "송선주":
    print(name + "님은 놀이 기구를 탈 수 있습니다.")
else:
    print(name + "님은 놀이 기구를 탈 수 없습니다.")
print("----------------------------------------")
    
# or 논리 연산자의 실습
# or 논리 연산자는 모든 조건 중에서 하나만 참이면 참을 반환한다. (중요)
# or 논리 연산자는 모든 조건이 거짓이어야만 거짓을 반환한다. (중요)
if age >= 15 or height >= 165 or name == "김로운":
    print(name + "님은 놀이 기구를 탈 수 있습니다.")
else:
    print(name + "님은 놀이 기구를 탈 수 없습니다.")
print("----------------------------------------")    
    
# 논리 부정 연산자인 not에 대한 실습
# 논리 부정 연산자인 not는 조건이 참이면 전체 조건식의 결과를 바대로 거짓으로 만들고
# 조건식의 결과가 거짓이라면 참으로 바꾸는 역할을 한다. (중요)
if not(1 == 1):
    print("참입니다.")
else:
    print("거짓입니다.")