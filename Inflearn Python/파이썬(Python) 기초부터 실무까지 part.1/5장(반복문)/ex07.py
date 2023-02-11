# 화씨온도-섭씨온도 변환 테이블을 출력하는 프로그램을 작성해보자.
# for 문을 사용하며, 실수로 나타내도록 한다.
# 화씨 0도부터 100도까지 10도 단위로 증가시키면서 대응되는 섭씨 온도를 출력하도록 하자.
# 공식 : C = (F - 32) * 5 / 9

for temp in range(0, 101, 10):
    c = (temp - 32) * 5.0 / 9.0
    print(temp, "\t", round(c, 2))