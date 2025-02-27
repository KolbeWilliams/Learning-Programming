#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// Declare and define your functions here:
// printRange
void printRange(int min, int max)
{
    int n = min;
    while (n <= max)
    {
        printf("%d ", n);
        n = n++;
    }
    printf("\n");
}
// largest
int largest(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    if (b > a)
    {
        return b;
    }
}
// smallest
int smallest(int k, int w)
{
    if (k < w)
    {
        return k;
    }
    if (w < k)
    {
        return w;
    }
}
// DO NOT CHANGE ANYTHING BELOW!
// The code down here has been provided for you to help you test
// your functions, and make sure that they're working correctly.
int main()
{
    printRange(5, 10); // 5, 6, 7, 8, 9, 10
    printRange(-2, 4); // -2, -1, 0, 1, 2, 3, 4
    printRange(5, 1); // should print nothing
    printf("---\n"); // Just to make the output easier to read
    int x = 6;
    int y = 4;
    printf("%d is larger than %d\n", largest(x, y), smallest(x, y));
    x = -12;
    y = 100;
    printf("%d is larger than %d\n", largest(x, y), smallest(x, y));
}