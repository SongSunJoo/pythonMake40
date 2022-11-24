# 숫자 맞추는 게임 코드 만들기
# import random

# random_number = random.randint(1, 100)

# game_count = 1

# while True:
#     my_number = int(input("1~100사이의 숫자를 입력하세요: "))
    
#     if my_number > random_number:
#         print("다운")
#     elif my_number < random_number:
#         print("업")
#     elif my_number == random_number:
#         print(f"정답입니다!! {game_count}번 만에 맞췄습니다.")
#         break
#     game_count = game_count + 1

# 이건 내가 코딩한 것
import random

random_number = random.randint(1, 100)

game_count = 1

while True:
    my_number = int(input("1~100까지의 숫자 중 하나를 입력하세요: "))
    if my_number > random_number:
        print("다운")
    elif my_number < random_number:
        print("업")
    else:
        print("정답입니다!!", game_count, "번 만에 맞췄습니다.")
        break
    game_count = game_count + 1