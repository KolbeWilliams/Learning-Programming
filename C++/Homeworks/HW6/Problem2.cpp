//DO NOT MODIFY THIS SECTION
#include <iostream>
#include <fstream>
using namespace std;

//prototypes (INSERT HERE IF YOU USE FUNCTIONS)
void lowestHighest(int[], int, int&, int&);
int totalNum(int[], int);
//end prototypes
int main()
{
    ifstream ifile;
    string fileName;
    int lowest, highest, total = 0, counter = 0, numbers[20];
    double average;
    cout << "Name of file: ";
    cin >> fileName;
    ifile.open(fileName);
    if (ifile.fail())
    {
        cout << "Error" << endl;
        return 1;
    }
    //ADD YOUR CODE FROM HERE
    //1. Read numbers from file, put them into the array, and determine the length of the array
    while (!ifile.eof())
    {
        ifile >> numbers[counter];
        counter++;
    }
    ifile.close();

    //2. Calculate the required values using function calls
    lowestHighest(numbers, counter, lowest, highest);
    total = totalNum(numbers, counter);
    average = total / static_cast<double>(counter);

    //3. Display output
    cout << "Lowest number: " << lowest << endl;
    cout << "Highest number: " << highest << endl;
    cout << "Total: " << total << endl;
    cout << "Average: " << average << endl << endl;
    cout << "File \"" << fileName << "\" for the example:" << endl << endl;
    for (int i = 0; i < counter; i++)
        cout << numbers[i] << endl;
    return 0;
}

//4. Write the lowestHighest function
void lowestHighest(int arr[], int length, int& low, int& high)
{
    //4.1 Pass variables by reference to hold the highest and lowest values
    low = high = arr[0];
    //4.2 Traverse through the array and compare each element to find the highest and lowest element
    for (int i = 0; i < length - 1; i++)
    {
        if (low > arr[i + 1])
            low = arr[i + 1];
        if (high < arr[i + 1])
            high = arr[i + 1];
    }
}

//5. Write the totalNum function
int totalNum(int arr[], int length)
{
    int sum = 0;
    //5.1 Traverse throught he array and add all of the elements together to get the total
    for (int i = 0; i < length; i++)
        sum += arr[i];
    return sum;
}