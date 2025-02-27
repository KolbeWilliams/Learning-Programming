#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void happyBirthday(int x)
{
	while (x <= 0)
	{
		printf("Please do not enter an integer less than or equal to zero:");
		scanf("%d", &x);
	}
	if (x > 0)
	{
		for (int i = 0; i < x; i++)
		{
			printf("Happy Birthday!\n");
		}
	}
}

double divide(double a, double b)
{
	if (b == 0)
	{
		printf("Cannot divide by zero ");
		return 0;
	}
	return a / b;
}

int main()
{
	int y;
	printf("How old are you?: ");
	scanf("%d", &y);
	happyBirthday(y);

	double z;
	double k;
	printf("Enter two numbers to divide them: \n");
	scanf("%lf %lf", &z, &k);
	divide(z, k);
	
	double answer = divide(z, k);
	printf("%lf", answer);
}