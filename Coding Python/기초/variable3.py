# dictionary 딕셔너리
# 사전 : key와 value의 형태로 구성
# 딕셔너리의 표현은 {} 중괄호로 데이터를 묶음
# {key1:value, key2:value, key3:value} 형태로 값을 묶음
# key값을 이용하여 value를 찾는다
a_dict = {'a':1, 'b':2, 'c':3}
print(a_dict)
print(a_dict['a'])
print(a_dict['b'])
print(a_dict['c'])

# 딕셔너리의 key값은 꼭 문자형태가 아닌 숫자도 가능
# 값은 숫자, 문자, 리스트 등 다양한 값을 넣을 수 있음
b_dict = {1:'a', 'b':[1,2,3], 'c':3}
print(b_dict[1])
print(b_dict['b'])
print(b_dict['c'])

# 새로운 key값과 데이터를 입력하여 딕셔너리에 데이터를 추가할 수 있음
b_dict['d'] = 4
print(b_dict['d'])
print(b_dict)

# set 집합
# 중복이 없는 자료형 set() 안에 [] 리스트 형태로 데이터를 넣어줌
a_set = set([1, 2, 3, 4])
print(a_set)

# 중복된 데이터를 넣어보자
b_set = set([1, 1, 1, 2, 2, 3, 3, 4, 5])
print(b_set)

# 순서대로 정렬하지 않음
# 실제 순서 없음
# 데이터를 순서대로 정렬해야 하는 곳에서는 사용 불가
c_set = set("python40s")
print(c_set)