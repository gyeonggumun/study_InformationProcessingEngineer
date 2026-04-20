#include <stdio.h>
int main() {
int a[] = {10, 20, 30, 40, 50};
int *p = a;
int x = *p++; //10
int y = *++p; //30
int z = ++*p; //31
printf("%d", x + y + z); 
// 71
return 0;
}
