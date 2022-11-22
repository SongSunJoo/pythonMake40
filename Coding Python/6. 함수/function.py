# 함수 : 코드가 모여 있는 하나의 단위
# 함수를 만들기 위해서는 def 이름:
# 코드에서 func()를 호출하면 함수 안에 정의된 코드를 실행
# def func():
#     print("안녕하세요.")
#     print("파이썬과 40개의 작품들 입니다.")
# func()

def func():
    print("안녕하세요.")
    print("파이썬과 40개의 작품들 입니다.")
for i in range(5):
    func()
    
# 함수에서 2개의 값을 받아 더한 값을 반환해주는 함수를 만들고 동작
def funcAdd(a, b):
    return a + b
c = funcAdd(20, 40)
print(c)

# 곱하는 함수
def funcMulti(d, e):
    return d * e
f = funcMulti(10, 33)
print(f)

# 파이썬의 함수는 여러 개의 값을 반환할 수 있음
# 숫자 두 개를 입력받아 더한값과 곱한값을 각각 반환하는 함수
def funcAddMulti(g, h):
    add = g + h
    mux = g * h
    return add, mux
g, h = funcAddMulti(44, 99)
print(g, h)

# 첫번째 반환값에는 i가 두번째 반환값에는 j가 저장되어 i에는 더한 값, j는 곱한 값이 저장됨
# 함수에서 반환되는 값 중에 선택하여 값을 받을 수 있음
def funcAddMulti2(i, j):
    plus = i + j
    mul = i * j
    return plus, mul
_,j = funcAddMulti2(7, 9)  # _,j를 사용해서 첫번째 값은 받지 않겠다는 의미, 고로 두번쨰 값만 받아 사용함
print(j)

# 연습
# 나누기와 나머지를 한 값을 각각 return해서 구해보기
def funcDivisionReinder(k, l):
    div = k / l
    ren = k % l
    return div, ren
k, l = funcDivisionReinder(2, 70)
print(k, l)

_,l = funcDivisionReinder(2, 70)
print(l)