# 비교연산
# == : 두개의 값이 같을 때 참
# >= : 왼쪽의 값이 크거나 같을 때 참
# <= : 오른쪽의 값이 크거나 같을 때 참
# > : 왼쪽의 값이 클 때 참
# < : 오른쪽의 값이 클 때 참
# != : 두 개의 값이 같지 않을 때 참
print(10 == 10)
print(10 >= 10)
print(10 <= 10)
print(10 > 10)
print(10 < 10)
print(10 != 10)

# in : 리스트나 문자열에서 포함된 값을 비교
# 리스트에서 값이 포함되어있는지 확인하는 코드
a_list = ['a', 2, 'hello', 3]
print('a' in a_list)
print(1 in a_list)
print('hello' in a_list)
print(3 in a_list)

# 문자열에서 문자가 포함되어 있는지 확인 가능
a_str = "hello python"
print("python" in a_str)
print("py" in a_str)
print("40" in a_str)