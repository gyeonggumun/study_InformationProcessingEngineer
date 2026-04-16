class Test {
    static int a = 1;
    int b = 1;

    Test() {
        a++;        // static → 모든 객체 공유 → 누적됨
        b++;        // instance → 객체마다 따로 증가
    }
}

public class Main {
    public static void main(String[] args) {
        Test t1 = new Test(); // a=2, t1.b=2
        Test t2 = new Test(); // a=3, t2.b=2

        System.out.println(t1.b + " " + t2.b + " " + Test.a);
        // 출력: 2 2 3
    }
}
