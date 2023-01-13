# 1~100까지 누적값을 구하는데 누적값이 2000이상이 되면 for 문을 빠져 나오는 프로그램을 작성하시오.
# 내가 한 것
hap = 0
for i in range(1, 101):
    hap += i
    if hap < 2000:
        print("1~100까지의 누적합 : ", hap)
    else:
        break

# 강의에서 한 것
hap = 0
# breakpoint(중단점)는 디버깅(에러를 잡아가는 과정)에 아주 효율적으로 사용할 수가 있다.
for i in range(101):
    # 2000이상이면 for 루푸를 빠져 나오는 코드
    if hap >= 2000:
        print("마지막으로 더해지는 i의 값: ", i)
        break
    else:
        hap += i

print("hap: ", hap)