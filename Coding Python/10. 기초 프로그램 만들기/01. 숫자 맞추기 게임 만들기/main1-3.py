# 게임 코드 트러블 슈팅
# try ~ expt

import random

random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력해 주세요.: "))
    
        if my_number > random_number:
            print("다운")
        elif my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"정답입니다!!! {game_count}번 만에 맞추셨습니다.")
        game_count = game_count + 1
    except:
        print("에러가 발생했습니다. 숫자를 입력해 주세요.")