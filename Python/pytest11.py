class A:
    def __init__(self):
        print("A", end="")

class B(A):
    def __init__(self):
        super().__init__() # 부모(A)의 생성자 호출
        print("B", end="")

class C(A):
    def __init__(self):
        super().__init__() # 부모(A)의 생성자 호출
        print("C", end="")

class D(B, C):
    def __init__(self):
        super().__init__() # 다중 상속 구조에서 다음 순서(B) 호출
        print("D", end="")

obj = D() # ACBD
