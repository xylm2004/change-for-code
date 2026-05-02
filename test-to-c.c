#include <stdio.h>
#include <stdlib.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    printf("Hello, C!\n");

    int x = 10, y = 20;
    printf("%d + %d = %d\n", x, y, add(x, y));

    int arr[] = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += arr[i];
    }
    printf("sum of array = %d\n", sum);

    return 0;
}
