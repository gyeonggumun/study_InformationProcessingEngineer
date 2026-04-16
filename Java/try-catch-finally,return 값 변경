public class Main {
    static int test() {
        int x = 1;
        try {
            return x;        // 반환값 1을 임시 저장
        } finally {
            x = 2;           // 변수 값 변경 (하지만 이미 반환값은 1로 결정됨)
        }
    }

    public static void main(String[] args) {
        System.out.println(test()); // 1
    }
}
