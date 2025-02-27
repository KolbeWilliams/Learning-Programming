#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void printArray(int* array, int length)
{
	for (int i = 0; i < length; i++)
	{
		printf("[%d] = %d\n", i, array[i]);
	}
	printf("\n\n");
}

int* ones(int length)
{
	int* array1 = malloc(length * sizeof(int));

	for (int i = 0; i < length; i++)
	{
		array1[i] = 1;
	}
	int* n = array1;
	return n;
}

int* sequence(int length)
{
	int* array1 = malloc(length * sizeof(int));

	array1[0] = 0;

	for (int i = 0; i < length; i++)
	{
		array1[i+1] = array1[i] + 1;
	}
	int* n = array1;
	return n;
}

void negate(int* array1, int length)
{
	for (int i = 0; i < length; i++)
	{
		array1[i] = -array1[i];
	}
}

int main()
{
	int X;
	int Y;
	
	//ones
	printf("Type in a number: ");
	scanf("%d", &X);
	int* n = ones(X);
	printArray(n, X);

	//sequence
	printf("Type in a number: ");
	scanf("%d", &Y);
	int* k = sequence(Y);
	printArray(k, Y);

	//negate
	negate(n, X);
	printArray(n, X);
	negate(k, Y);
	printArray(k, Y);

	free(n);
	n = NULL;
	free(k);
	k = NULL;
}