# import를 이용하여 외부에서 라이브러리, 모듈 등을 불러와 사용할 수 있다.
# random 라이브러리는 무작위 값을 반환
import random
print(random.randint(1, 100))

# rd라는 이름으로 불러보기
import random as rd
print(rd.randint(1, 100))

# from import
# 특수한 기능만 불러와 봄
from random import randint
print(randint(1, 100))

# 모든 기능을 불러와봄
from random import *
print(randint(1, 100))