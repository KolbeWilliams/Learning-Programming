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

int main()
{
	char username[21];
	char copy[21];
	//get username
	printf("Type in your username: ");
	scanf("%s", &username);

	//copy the username
	strcpy(copy, username);

	//capitalize the username
	char* newUser = capitalize(copy);
	printf("Original: %s\n", username);
	printf("Copy: %s\n", newUser);
}