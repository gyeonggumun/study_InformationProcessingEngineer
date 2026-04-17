class A {
    int x = 1;

    int get() {
        return x;
    }
}

class B extends A {
    int x = 2;

    int get() {
        return x;
    }
}

public class Main {

    static void change(A obj) {
        obj.x += 10;   // A.x = 11 (원본 영향 O)
        obj = new B(); // 새로운 객체 (원본 끊김)
        obj.x += 20;   // 새 객체 A.x = 21 (원본 영향 X)
    }

    public static void main(String[] args) {
        A obj = new B();

        change(obj);

        System.out.println(obj.x + " " + obj.get());
        // obj.x → 11 (A 기준)
        // obj.get() → 2 (B 기준)
    }
}
