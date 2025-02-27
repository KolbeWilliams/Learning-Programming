//DO NOT MODIFY THIS SECTION
#include <iostream>
#include <fstream>
using namespace std;

struct Weather
{
    int rainfall;
    int hTemp;
    int lTemp;
    float avg;
};

//prototypes (USE ONLY IF YOU WILL USE FUNCTIONS)
int highTemp(Weather[], int, int&);
int lowTemp(Weather[], int, int&);
float averageTemp(Weather[], int, float);

int main()
{
    //USE THIS DATA ONLY FOR TESTS.
    //THE DATA MUST BE INTRODUCED BY THE USER OR FROM FILE
    /*Weather year[12] = {200,  90, 60, 0.0,
                            300,  95, 62, 0.0,
                            200,  99, 65, 0.0,
                            200, 101, 66, 0.0,
                            400, 105, 67, 0.0,
                            600, 108, 70, 0.0,
                            700, 112, 72, 0.0,
                            700, 111, 74, 0.0,
                            400, 108, 72, 0.0,
                            200, 104, 68, 0.0,
                            200,  98, 66, 0.0,
                            100,  92, 64, 0.0 };*/
    //ifstream ifile;
    int highest, lowest, totalRain = 0, fullAverage;
    float sumAvg = 0;
    //ADD YOUR CODE FROM HERE
    //1. Initialize highest, lowest, and fullAverage variables for later use, and declare the array
    highest = lowest = 0;
    fullAverage = 12;
    Weather year[12];

    //2. Use a for loop to traverse the array and ask the user for input about each month
    for (int i = 0; i < 12; i++)
    {
        cout << "Enter rainfall, highest and lowest temperature for month number #" << i + 1 << ": ";
        //2.1 Use a do-while loop for input validation with the high and low temperatures
        do {
            cin >> year[i].rainfall;
            cin >> year[i].hTemp;
            cin >> year[i].lTemp;
            if (year[i].hTemp < -100 || year[i].hTemp > 140 || year[i].lTemp < -100 || year[i].lTemp > 140)
                cout << "Please reenter rainfall, highest and lowest temperature for month number #" << i + 1 << " with high and low temperature between -100 and 140 degrees: ";
        } while (year[i].hTemp < -100 || year[i].hTemp > 140 || year[i].lTemp < -100 || year[i].lTemp > 140);
        //2.2 Use the user input to calculate the average temperature for each month
        year[i].avg = (static_cast<float>(year[i].hTemp) + year[i].lTemp) / 2;
    }

    //3. Display the temperature averages for each month using another for loop
    cout << "Averages of the year: " << endl;
    for (int i = 0; i < 12; i++)
    {
        cout << "   " << year[i].avg << endl;
        //3.1 Calculate the total rainfall within the same for loop
        totalRain += year[i].rainfall;
    }

    //4. Display the results by calling the highTemp, lowTemp, and averageTemp functions
    cout << "Total rainfall: " << totalRain << endl;
    cout << "Highest temperature: " << highTemp(year, 12, highest) << " on month #" << highest << endl;
    cout << "Lowest  temperature: " << lowTemp(year, 12, lowest) << " on month #" << lowest << endl;
    cout << "Average temperature: " << averageTemp(year, fullAverage, sumAvg) << endl;

    return 0;
}

//5. Write the hightemp function
int highTemp(Weather year[], int size, int &hMonth)
{
    //5.1 Set the hMonth variable that was passed by reference to the first month
    int i = 0;
    hMonth = 1;
    int high = year[i].hTemp;
    //5.2 Traverse the array and find the highest temperature from the year
    for (i = 1; i < size; i++)
    {
        if (year[i].hTemp > high)
        {
            //5.3 Set the highest temperatue and month variables when found
            high = year[i].hTemp;
            hMonth = i + 1;
        }
    }
    return high;
}

//6. Write the lowTemp function
int lowTemp(Weather year[], int size, int &lMonth)
{
    //6.1 set the lMonth variable that was passed by reference to the first month
    int i = 0;
    lMonth = 1;
    int low = year[i].lTemp;
    //6.2 Traverse the array to find the lowest temperature from the year
    for (i = 1; i < size; i++)
    {
        if (year[i].lTemp < low)
        {
            //6.3 Set the lowest temperature and month variables when found
            low = year[i].lTemp;
            lMonth = i + 1;
        }
    }
    return low;
}

//7. Write the average Temp function
float averageTemp(Weather year[], int fullAverage, float sumAvg)
{
    //7.1 Traverse the array and add all of the average temperature for each month together
    for (int i = 0; i < fullAverage; i++)
        sumAvg += year[i].avg;
    //7.2 Returen the sum of the average temperature for the year divided by 12
    return sumAvg / fullAverage;
}