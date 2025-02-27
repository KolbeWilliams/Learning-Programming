/*//DO NOT MODIFY THIS SECTION
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
using namespace std;

//prototypes (USE ONLY IF YOU WILL USE FUNCTIONS)
char* mystrtok(char* str);
void extractWords(char* s);

int main()
{
    string input, separated;
    cout << "Type the sentence (no spaces): ";
    cin >> input;
    //ADD YOUR CODE FROM HERE
    int length = input.length();
    char* output = new char[length];

    extractWords(output);

    return 0;
}

char* mystrtok(char* str)
{
    static char* input = NULL;
    if (str != NULL) {
        input = str;
    }

    // Base case
    if (input == NULL)
        return NULL;

    // Array for storing tokens
    // +1 is for '\0'
    char* output = new char[strlen(input + 1)];

    int i = 0;

    // Storing the upper case character
    output[i] = input[i];

    i++;

    // Generating Tokens
    for (; input[i] != '\0'; i++) {
        if (!isupper(input[i]))
            output[i] = input[i];
        else {
            output[i] = '\0';
            input = input + i;
            return output;
        }
    }

    output[i] = '\0';
    input = NULL;
    return output;
}

void extractWords(char* s)
{

    // Extract 1st word and print it
    char* ptr = mystrtok(s);
    cout << ptr << endl;

    // Extract the remaining words
    while (ptr != NULL) {
        ptr = mystrtok(NULL);
        cout << ptr << endl;
    }
}*/