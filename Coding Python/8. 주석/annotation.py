# 주석 : 프로그래밍 문법과는 상관없이 프로그램 설명이나 코드 자체를 실행하지 못하게 하는 용도로 사용
# 주석입니다. #으로 표현
# 사용자 설명 코드 입니다.
# print("hello")  # 코드의 줄 끝에 사용할 수 있습니다.
print("hi")

# 여러 줄을 주석처리 할 때는 """ 쌍따옴표 3개로 시작하고 """ 쌍다옴포 3개로 종료
"""
    여러 줄을 입력할 때는
    쌍따옴표 3개로 시작하고
    쌍따옴표 3개로 종료하면
    여러 줄을 입력할 수 있습니다.
"""

# ''' ''' 따옴표 3개로 시작하고 3개로 종료해도 동일

'''
    또는 여러 줄을 입력할 때는
    따옴표 3개로 시작하고
    따옴표 3개로 종료하면
    여러 줄을 입력할 수 있습니다.
'''

a_str = """
여러 줄의
문자열을 입력할 때도
쌍따옴표 또는 따옴표
3개를 사용할 수 있습니다.
"""
print(a_str)

# 원하는 부분만 주석할 때는 ctrl + / 눌러서 주석 지정 및 해제 가능
# 맥에서는 command + /
