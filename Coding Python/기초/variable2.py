# list 리스트
a_list = [1, 2, 3, 4, 5]
print(a_list)
print(a_list[0])
print(a_list[3])

# 리스트의 데이터를 자를 수 있음
# 처음부터 2번째 전까지의 데이터를 가져옴
print(a_list[:2])
# 2번째부터 마지막까지의 데이터를 가져옴
print(a_list[2:])

# 빈 리스트를 생성하고 데이터를 하나씩 추가하여 넣기
b_list = []
# b_list에 숫자 1,2,3을 넣는다
b_list.append(1)
b_list.append(2)
b_list.append(3)
print(b_list)

# 여러 타입의 변수 형태 저장
c_list = [1, 3.14, "hello", [1,2,3]]
print(c_list)
# 1번지부터 3번지 전까지의 데이터를 가져옴 1, 2번지의 데이터를 가져옴
print(c_list[1:3])

# 리스트는 데이터를 변경할 수 있음
d_list = [1, 2, 3, 4, 5]
print(d_list)
d_list[0] = 5
print(d_list)

# Tuple 튜플
# 소괄호 ()로 데이터를 묶음
# 리스트와 비슷하나 데이터를 변경할 수 없음
a_tuple = (1, 2, 3, 4, 5)
print(a_tuple)
a_tuple[0] = 10
print(a_tuple)