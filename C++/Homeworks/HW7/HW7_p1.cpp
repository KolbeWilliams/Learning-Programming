/*//DO NOT MODIFY THIS SECTION
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
using namespace std;

//prototypes (USE ONLY IF YOU WILL USE FUNCTIONS)

int main()
{
    string input, separated;
    cout << "Type the sentence (no spaces): ";
    cin >> input;
    //ADD YOUR CODE FROM HERE
    //1. Find the size of the input and put it in a constant variable
    const int SIZE = input.size();

    //2. Use a for loop to traverse the input
    for (int i = 0; i < SIZE; i++)
    {
        //2.1 Check if the character is an uppercase letter
        if (isupper(input[i]))
        {
            //2.1.1 On the first letter, simply add the character to the new string
            if (i == 0)
            {
                separated += input[i];
            }
            //2.1.2 On the rest of the uppercase letters, add a space and then the character to the
            //new string in lowercase
            else 
            {
                separated += ' ';
                separated += tolower(input[i]);
            }
        }
        //2.2 If the character isn't an uppercase letter, add the character to the new string
        else
            separated += input[i];
    }


    //3. Print the new, separated string
    cout << separated << endl;

    return 0;
}*/