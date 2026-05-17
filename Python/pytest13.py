def outer_func():
    count = 10
    
    def inner_func():
        nonlocal count # 바로 바깥 함수의 지역 변수를 사용
        count += 5
        return count
    
    print(inner_func(), end=" ") # 첫 번째 호출: 10 + 5
    print(count)                # 수정된 count 출력
# 15 15
outer_func()
