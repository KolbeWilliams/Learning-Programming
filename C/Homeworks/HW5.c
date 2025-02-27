#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* getline()
{
	// How large is our dynamic array?
	int arraySize = 8;
	// What's the actual length of our string?
	int stringLength = 0;
	char* str = malloc(sizeof(char) * arraySize);
	if (str == NULL)
	{
		printf("Something bad happened.\n");
		exit(0);
	}
	while (1)
	{
		char c;
		scanf("%c", &c);
		if (c == '\n')
		{
			if (stringLength > 0)
			{
				// We reached the end of the line
				break;
			}
		}
		else
		{
			// If our array isn't big enough, resize it
			// We're adding 1 to stringLength to account for the null character
			if (stringLength + 1 >= arraySize)
			{
				arraySize = arraySize * 2;
				str = realloc(str, arraySize);
				if (str == NULL)
				{
					printf("Something bad happened.\n");
					exit(0);
				}
			}
			// Add the new character to the array
			str[stringLength] = c;
			stringLength++;
		}
	}
	// Add the null character at the end of our string
	// We don't have to think about resizing the array, because we already
	// reserved an extra character of space at the end
	str[stringLength] = '\0';
	return str;
}

//if user enters q or Q
char* censorQ(char* string)
{
	for (int i = 0; string[i] != '\0'; i++)
	{
		if (string[i] == 'q' || string[i] == 'Q')
		{
			for (int n = 0; string[n] != '\0'; n++)
			{
				if (string[n] != ' ')
				{
					string[n] = '*';
				}
			}
		}
	}
	return string;
}

int main()
{
	//Ask user for their name
	printf("Type in your name (it can only contain letters!): ");
	char* name = getline();

	//Check if name only contains letters
	int count = 0;
	for (int i = 0; name[i] != '\0'; i++)
	{
		if (isalpha(name[i]) == 0)
		{
			if (name[i] != ' ')
			{
				count = 1;
			}
		}
	}
	while (count == 1)
	{
		printf("Type in your name (it can only contain letters!): ");
		name = getline();
		int count2 = 0;
		for (int i = 0; name[i] != '\0'; i++)
		{
			if (isalpha(name[i]) == 0)
			{
				if (name[i] != ' ')
				{
					count2 = 1;
				}
			}
		}
		count = count2;
	}

	//Printing messages
	printf("Type as many messages as you like! Type !help for more info.\n");
	printf(">");
	char* message = getline();
	int format = 0;
	while (strcmp(message, "!exit") != 0 && strcmp(message, "!EXIT") != 0)
	{

		censorQ(message);

		//for determining output
		if (strcmp(message, "!help") == 0)
		{
			format = 1;
		}
		else if (strcmp(message, "!yell") == 0)
		{
			format = 2;
		}
		else if (strcmp(message, "!whisper") == 0)
		{
			format = 3;
		}
		else if (strcmp(message, "!normal") == 0)
		{
			format = 4;
		}

		//for default
		if (format == 0)
		{
			printf("(%s): %s\n", name, message);
			printf(">");
			message = getline();
		}

		// for !help command
		else if (format == 1)
		{
			printf("Here are the commands:\n");
			printf("	!yell to convert your messages to UPPERCASE\n");
			printf("	!whisper to convert your messages to lowercase\n");
			printf("	!normal to stop yelling or whispering\n");
			printf("	!exit to leave\n");
			printf(".. Oh - and don't type the letter Q :\n");

			format = 0;
			printf(">");
			message = getline();
		}

		//for !yell command
		else if (format == 2)
		{
			printf(">");
			message = getline();
			censorQ(message);
			if (strcmp(message, "!exit") == 0)
			{
				break;
			}
			for (int i = 0; message[i] != '\0'; i++)
			{
				if (message[i] >= 'a' && message[i] <= 'z')
				{
					message[i] = toupper(message[i]);
				}
			}
			if (strcmp(message, "!HELP") == 0)
			{
				format = 1;
			}
			else if (strcmp(message, "!WHISPER") == 0)
			{
				format = 3;
			}
			else if (strcmp(message, "!NORMAL") == 0)
			{
				format = 4;
			}
			else
			{
				printf("(%s): %s\n", name, message);
			}
		}

		//for !whisper command
		else if (format == 3)
		{
			printf(">");
			message = getline();
			censorQ(message);
			if (strcmp(message, "!EXIT") == 0)
			{
				break;
			}
			for (int i = 0; message[i] != '\0'; i++)
			{
				if (message[i] >= 'A' && message[i] <= 'Z')
				{
					message[i] = tolower(message[i]);
				}
			}
			if (strcmp(message, "!help") == 0)
			{
				format = 1;
			}
			else if (strcmp(message, "!yell") == 0)
			{
				format = 2;
			}
			else if (strcmp(message, "!normal") == 0)
			{
				format = 4;
			}
			else
			{
				printf("(%s): %s\n", name, message);
			}
		}

		//for !normal command
		else if (format == 4)
		{
			printf(">");
			message = getline();
			censorQ(message);
			if (strcmp(message, "!help") == 0)
			{
				format = 1;
			}
			else if (strcmp(message, "!yell") == 0)
			{
				format = 2;
			}
			else if (strcmp(message, "!whisper") == 0)
			{
				format = 3;
			}
			else
			{
				printf("(%s): %s\n", name, message);
			}
		}
	}
	//for !exit command
	printf("Goodbye!");
	free(name);
	free(message);
}