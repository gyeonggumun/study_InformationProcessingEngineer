class A {
    A(int x) {
        System.out.print(x + " ");
    }
}

class B extends A {
    B() {
        super(10); // 부모 생성자 먼저 호출
        System.out.print("B");
    }
}

public class Main {
    public static void main(String[] args) {
        new B(); // 10 B
    }
}
