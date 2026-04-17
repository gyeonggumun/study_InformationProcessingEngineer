class A {
    int x = 5;

    int getX() {
        return x;
    }
}

class B extends A {
    int x = 10;

    int getX() {
        return super.x + x; // A.x(5) + B.x(10)
    }
}

public class Main {
    public static void main(String[] args) {
        A obj = new B();

        System.out.println(obj.getX()); // 15
    }
}
