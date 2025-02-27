#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// multiplyArray
void multiplyArray(int* array, int length, int X)
{

	for (int i = 0; i < length; i++)
	{
		array[i] = array[i] * X;
	}
}
// printArray
void printArray(int* array, int length)
{
	for (int i = 0; i < length; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n\n");
}

// addArrays
void addArrays(int* array1, int* array2, int length)
{
	for (int i = 0; i < length; i++)
	{
		array1[i] = array1[i] + array2[i];
	}
}

// Please do *not* change anything below!
// These tests are provided to ensure your code is working correctly.
// If you change this code, you will receive a zero on your submission.
int main()
{
	int A[5] = { 2, 4, 6, 8, 10 };
	int B[5] = { 1, 2, 3, 4, 5 };
	int C[3] = { 7, 8, 6 };

	//A should now be { 4, 8, 12, 16, 20}
	multiplyArray(A, 5, 2);

	//A should now be {5, 10, 15, 20, 25}
	addArrays(A, B, 5);

	//C should now be { 21, 24, 18 }
	multiplyArray(C, 3, 3);

	//Print all of the arrays
	printArray(A, 5);
	printArray(B, 5);
	printArray(C, 3);
}