class A {
    int x = 10;

    int getX() {
        return x;
    }
}

class B extends A {
    int x = 20;

    int getX() {
        return x;
    }
}

public class Main {
    public static void main(String[] args) {
        A obj = new B();

        System.out.println(obj.x);      // 10 → 변수는 참조타입 A 기준
        System.out.println(obj.getX()); // 20 → 메서드는 실제 객체 B 기준
    }
}
