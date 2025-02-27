//DO NOT MODIFY THIS SECTION
#include <iostream>
using namespace std;
const double BROKER_COMM = 2.0;
int main()
{
    double shares, pricePerShare;
    double amountPaid, amountComm, totalPaid;
    //ADD YOUR CODE FROM HERE
    cout << "Enter the amount of shares bought: ";
    cin >> shares;
    cout << "\nEnter the price per share in dollars: ";
    cin >> pricePerShare;

    amountPaid = shares * pricePerShare;    //calculates the amount paid in stocks alone
    cout << "\nThe amount paid for the stock alone is: $" << amountPaid;
    amountComm = amountPaid * (BROKER_COMM / 100);  //calculates the amount paid in commission
    cout << "\nThe amount of commission is: $" << amountComm;
    totalPaid = amountPaid + amountComm;    //calculates the total amount paid
    cout << "\nThe total amount paid is: $" << totalPaid;
    return 0;
}