//DO NOT MODIFY THIS SECTION
/*#include <iostream>
using namespace std;

//prototypes (USE ONLY IF YOU WILL USE FUNCTIONS)
void read(double[]);
double total(double[]);
void highLow(double[], int&, int&);

int main()
{
    //initialization only for tests, commenting the input part
    double rainfall[12];//={2.3, 5.6, 8.2, 15.2, 4.7, 3.7, 6.8, 3.1, 1.1, 6.6, 2.7, 5.5 };
    int max, min;
    //ADD YOUR CODE FROM HERE
    //1. Ask user to input data
    read(rainfall);

    //2. Print the results based on the entered data
    cout << "Total: " << total(rainfall) << endl;
    cout << "Average: " << total(rainfall) / 12 << endl;
    highLow(rainfall, max, min);
    cout << "Highest month: " << max << endl;
    cout << "Lowest month: " << min << endl;
    return 0;
}

//3. Define functions
//3.1 Write the read function
void read(double arr[])
{
    for (int i = 0; i < 12; i++)
    {
        //3.1.1 Ask for the rainfall for each month and store it in an array
        //3.1.2 Use a do while loop for input validation
        do {
            cout << "Rainfall month " << i + 1 << ": ";
            cin >> arr[i];
            if (arr[i] < 0)
                cout << "Please do not enter a negative number for the rainfall for this month." << endl;
        } while (arr[i] < 0);
    }
}

//3.2 Write the total function
double total(double arr[])
{
    //3.2.1 Add all of the elements of the array together to get the total
    double sum = 0.0;
    for (int i = 0; i < 12; i++)
        sum += arr[i];
    return sum;
}

//3.3 Write the highLow function
void highLow(double arr[], int& high, int& low)
{
    //3.3.1 Initialize variables for the high and low values
    double highValue = arr[0];
    double lowValue = arr[0];
    for (int i = 0; i < 11; i++)
    {
        //3.3.2 Go through each element of the array and reassign the highest value if necessary
        if (highValue < arr[i + 1])
        {
            highValue = arr[i + 1];
            //3.3.3 identify the number of the highest month and assign it to the reference variable
            high = i + 2;
        }
        //3.3.4 Repeat the steps used to find the mighest rainfall month for the lowest rainfall month
        if (lowValue > arr[i + 1])
        {
            lowValue = arr[i + 1];
            low = i + 2;
        }
    }
}*/