#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30};
    int *p = arr;  // 배열 이름은 첫 번째 요소 주소 → &arr[0]

    printf("%d ", *p);        // 10 → p가 arr[0] 가리킴
    printf("%d ", *(p + 1));  // 20 → 다음 요소
    printf("%d ", p[2]);      // 30 → p[2] == *(p + 2)

    return 0;
}
