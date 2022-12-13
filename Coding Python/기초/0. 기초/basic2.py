# 자연수 13이 홀수인지 짝수인지 판별

num = 13
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

print("=========================")

# 홍길동 씨의 과목별 점수로 평균 점수 구해보기

profile = {"국어":80, "영어":75, "수학":55}

temp = 0
for v in profile.values():
    temp += v
print(len(profile)) # 과목수 3개
temp /= len(profile)

print(profile.values())

print(temp)