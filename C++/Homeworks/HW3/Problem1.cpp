//DO NOT MODIFY THIS SECTION
#include <iostream>
using namespace std;

int main()
{
    int firstTime, secondTime, thirdTime;

    string runnerOne, runnerTwo, runnerThree;

    //ADD YOUR CODE FROM HERE
    //1. Ask user for runner names and times
    do
    {
        cout << "Runner number 1: ";
        cin >> runnerOne;
        cout << "Time: ";
        cin >> firstTime;
        cout << "Runner number 2: ";
        cin >> runnerTwo;
        cout << "Time: ";
        cin >> secondTime;
        cout << "Runner number 3: ";
        cin >> runnerThree;
        cout << "Time: ";
        cin >> thirdTime;

        if (firstTime < 0 || secondTime < 0 || thirdTime < 0)
            cout << "Please enter positive values for the runner's times." << endl;
    } while (firstTime < 0 || secondTime < 0 || thirdTime < 0);

    //2. Calculate race results
    string first, second, third;
    
    if (firstTime < secondTime && firstTime < thirdTime)
        first = runnerOne;
    else if (secondTime < firstTime && secondTime < thirdTime)
        first = runnerTwo;
    else if (thirdTime < firstTime && thirdTime < secondTime)
        first = runnerThree;

    if (first == runnerOne)
        secondTime < thirdTime ? (second = runnerTwo, third = runnerThree) : (second = runnerThree, third = runnerTwo);
    else if (first == runnerTwo)
        firstTime < thirdTime ? (second = runnerOne, third = runnerThree) : (second = runnerThree, third = runnerOne);
    else if (first == runnerThree)
        secondTime < firstTime ? (second = runnerTwo, third = runnerOne) : (second = runnerOne, third = runnerTwo);
    
    //3. Display race results
    cout << "Results:" << endl;
    cout << "1st Place: " << first << endl;
    cout << "2nd Place: " << second << endl;
    cout << "3rd Place: " << third << endl;
    return 0;
}