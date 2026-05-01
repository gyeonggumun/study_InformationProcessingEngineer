x = 100 # 전역 변수

def func():
    global x # 전역 변수 x를 사용하겠다고 선언
    x = 200  # 전역 변수 x의 값을 200으로 변경
    y = 50   # 지역 변수 y
    return x + y

func() # 여기서 전역 변수 x가 200으로 바뀜
print(x) #200
