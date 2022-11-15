a = 10
b = 10
c = a + b
print(c)

d = '10'
# 숫자와 문자열은 더할 수 없어서 에러
# print(c + d)
print(c + int(d))
print(str(c) + d)

e = 3.14
f = 10
print(e + f)

a = 10
b = 10
c = a + b
print(c)

a = 10
b = 10
c = float(a) + float(b)
print(c)

a_bool = True
b_bool = False
a_int = 1
b_int = 0
print(a_bool)
print(b_bool)
print(type(a_bool))
print(type(b_bool))
print(a_int)
print(b_int)
print(type(a_int))
print(type(b_int))