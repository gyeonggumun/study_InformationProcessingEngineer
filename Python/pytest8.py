def func(n):
    return lambda a : a ** n   # n제곱을 수행하는 익명 함수 반환

f2 = func(2)  # a^2 함수 생성
f3 = func(3)  # a^3 함수 생성

# f2(3) = 3^2 = 9
# f3(2) = 2^3 = 8
print(f2(3) + f3(2)) 
