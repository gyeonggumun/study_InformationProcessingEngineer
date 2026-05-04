class Counter:
    count = 0                     # 클래스 변수
    def __init__(self):
        Counter.count += 1        # 생성 시 클래스 변수 증가
        self.num = Counter.count  # 인스턴스 변수에 현재 클래스 변수 저장

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(c1.num + c2.num + Counter.count) # 1 + 2 + 3 = 6
