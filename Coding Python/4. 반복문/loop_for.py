# for : 반복되는 부분이나 범위를 구체적으로 지정해서 실행
for i in range(7):
    print(i)
    
# range 범위 지정 range(시작, 끝(-1))
for i in range(10, 20):
    print(i)
    
# for문의 i값은 요소를 출력, i의 이름은 원하는 대로 변경 가능
# range 함수의 3번째 인자에 -1을 입력하면 역순으로 출력 가능
for i in range(10, 5, -1):
    print(i)
    
# 리스트에서 for문을 이용하여 값을 가져오는 방법
a_list = [1, 2, 3, 4, 5, "안녕", "하세요"]
for i in a_list:
    print(i)
    
# for문을 이용하여 문자의 수만큼 반복 가능
a_str = "hello python"
for i in a_str:
    print(i)
    
# enumerate를 이용하면 리스트에서 위치와 값을 가져올 수 있음
name_list = ["송선주", "김석우", "유연석"]
age_list = [34, 37, 38]
for i,k in enumerate(name_list):
    print("i=", i, end=' ')
    print("k=", k)
    
for i,k in enumerate(name_list):
    print(k, end=' ')
    print(age_list[i])
for i,k in enumerate(name_list):
    print(name_list[i], end=' ')
    print(age_list[i])
    
# 위 방법은 헷갈릴 수 있어 k값은 사용하지 않고, 증가되는 값인 i만 이용하여 리스트에서 값을 가져옴
# enumerate 사용하지 않고 list의 길이만큼 range에 입력하여 사용할 수 있음
for i in range(len(name_list)):
    print(name_list[i], end=' ')
    print(age_list[i])
# range(len(name_list))와 같이 name_list의 길이를 range함수에 입력하여 for문 반복

# 한줄의 for문을 이용하여 리스트의 값을 쉽게 넣을 수 있음
test_list = [i for i in range(10)]
print(test_list)

# .append : 리스트에 값을 넣을 때 사용하며 순차적으로 들어감
# 리스트를 만들고 초기에 원하는 값을 넣을 때 많이 사용
test2_list = []
for i in range(10):
    test2_list.append(i)    
print(test2_list)

# 10개의 데이터를 i에 5를 곱한 값으로 초기화
test3_list = [i * 5 for i in range(10)]
print(test3_list)

# 10개의 데이터를 0으로 초기화
test4_list = [0 for i in range(10)]
print(test4_list)
