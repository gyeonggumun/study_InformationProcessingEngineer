public class Main {
    public static void main(String[] args) {
        String str1 = "java";
        String str2 = "java";
        StringBuilder sb = new StringBuilder("java");

        System.out.print(str1 == str2);         // true  → 문자열 리터럴은 같은 주소 (String Pool)
        System.out.print(" ");
        System.out.print(str1.equals(sb));      // false → String vs StringBuilder (타입 다름)
        System.out.print(" ");
        System.out.print(sb.toString().equals(str1)); // true → 문자열로 변환 후 비교
    }
}
