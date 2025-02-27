#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* capitalize(char* string)
{
	for (int i = 0; string[i] != '\0'; i++)
	{
		if (string[i] >= 97 && string[i] <= 122)
		{
			char capLetter = string[i] - 32;
			string[i] = capLetter;
		}
		else
		{
			string[i] = string[i];
		}
	}
	return string;
}

int digits(char* string)
{
	int n = 0;
	for (int i = 0; i < strlen(string); i++)
	{
		if (string[i] >= 48 && string[i] <= 57)
		{
			n++;
		}
	}
	return n;
}

int main()
{
	char username[21];
	char copy[21];
	//get username
	printf("Type in your username: ");
	scanf("%s", &username);
	printf("\n");

	//copy the username
	strcpy(copy, username);

	//capitalize the username
	char* newUser = capitalize(copy);
	printf("Original: %s\n", username);
	printf("Copy: %s\n", newUser);

	//say if username has digits
	int n = digits(newUser);
	if (n > 0)
	{
		printf("The username has digits.\n");
	}
	else
	{
		printf("The username does *not* have digits.\n");
	}

	//length of the username
	printf("The username is %d characters long.\n", strlen(username));

	//first and last character
	printf("The first character is %c\n", username[0]);
	printf("The last character is %c\n", username[strlen(username)-1]);
}