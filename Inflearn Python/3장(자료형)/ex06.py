# 문자열의 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각에 해당하는 문자에 번호(인덱스)가 존재한다.
# [인덱스] 하면 문자열에서 문자를 추출할 수가 있다.
# 인덱스라 함은 무조건 0부터 시작이 된다. 마지막 인덱스는 n-1이 성립된다.
# 파이썬 특수기능인 인덱스를 처리할 때 음수도 사용이 가능하다.

word = "Python"
print(len(word))

print(word[0])
print(word[5])

# len(word)는 어차피 문자열의 길이인 6을 반환을 하기 때문에 -1을 해주면 끝문자를 반환해준다.
print(word[len(word)-1])

# 해당 문자열의 인덱스 범위 밖에 값을 주면 index out of range 라는 에러가 발생한다.
# print(word[100])

# 파이썬에서는 한 번 작성된 문자열은 변경이 불가능하다.
# word[2] = 'B'

# 사용자로부터 문자열 입력을 3개 받도록 한다.
# 각 해당 문자열의 첫 번째 문자를 인덱싱하여 문자를 합쳐서 문자열을 만드는 프로그램을 만들어보자.
item1 = input("첫 번째 단어를 입력하시오 : ")
item2 = input("두 번째 단어를 입력하시오 : ")
item3 = input("세 번쨰 단어를 입력하시오 : ")

word = item1[0] + item2[0] + item3[0]
print("새로 만든 문자열 : " + word)