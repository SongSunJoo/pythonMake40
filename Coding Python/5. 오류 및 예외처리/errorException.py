# 의도적으로 에러코드 발생
try:
    adjpfoaewp1
except:
    print("에러발생")

# 에러 무시    
try:
    adjpfoaewp1
except:
    pass
print("에러무시")

# 에러 원인
try:
    adjpfoaewp1
except Exception as e:
    print("에러발생 원인:", e)