#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define ARRAY_SIZE 10
int main()
{
	int array[ARRAY_SIZE];
	for (int i = 0; i < ARRAY_SIZE; i++)
	{
		printf("Type in a number to add to the array: \n");
		scanf("%d", &array[i]);
	}
	
	int n = array[0];
	for (int i = 0; i < ARRAY_SIZE; i++)
	{
		printf("%d\n", array[i]);
	}

	int x = array[0];
	int y = array[0];
	int add = 0;
	for (int i = 0; i < ARRAY_SIZE; i++)
	{
		if (x < array[i])
		{
			x = array[i];
		}
		if (y > array[i])
		{
			y = array[i];
		}
		add = add + array[i];
	}
	printf("%d is the smallest element in the array\n", y);
	printf("%d is the largest element in the array\n", x);
	printf("The sum off all the numbers in the array is: %d\n", add);
	printf("The memory address of the smallest number is %p\n", &y);
	printf("The memory address of the largest number is %p\n", &x);
	printf("The memory address of the first element in the array is %p\n", &array[0]);
	printf("The memory address of the last element in the array is %p\n", &array[9]);
}