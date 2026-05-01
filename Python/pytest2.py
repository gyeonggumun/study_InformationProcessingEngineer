class Parent:
    def __init__(self):
        self.value = 10
    def get_value(self):
        return self.value

class Child(Parent):
    def __init__(self):
        super().__init__() # 부모의 생성자 호출 (self.value = 10)
        self.value = 20    # 자식에서 value를 20으로 덮어씀
    def get_value(self):
        return self.value + 10 # 부모 메서드를 오버라이딩

obj = Child()
print(obj.get_value()) # 20 + 10이 실행되어 30
