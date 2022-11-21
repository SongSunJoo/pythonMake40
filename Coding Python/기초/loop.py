# while : 참과 거짓을 기준으로 조건이 거짓이 되기 전까지 무한 반복적으로 실행
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