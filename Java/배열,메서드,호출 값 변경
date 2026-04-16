public class Main {

    static void change(int[] arr) {
        arr[0] = 100;     // 배열 내부 값 변경 → 원본 영향 O
        arr = new int[]{9, 9, 9}; // 새로운 배열 생성 → 지역 변수만 변경됨
    }

    public static void main(String[] args) {
        int[] data = {1, 2, 3};

        change(data);

        System.out.println(data[0]); // 100 → 첫 줄은 반영됨, 두 번째 재할당은 반영 안됨
    }
}
