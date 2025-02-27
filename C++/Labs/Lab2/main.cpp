#include <iostream>
#include "Coin.h"
using namespace std;

int main()
{
	srand(time(nullptr));

	//1. Declare and initialize balance variable and create objects of coin class
	double balance = 0.0;
	Coin quarter;
	Coin dime;
	Coin nickle;

	//2. Use a while loop to flip the coins until it is >= 1
	while (balance < 1.0)
	{
		//2.1 Toss each coin and update the balance accordingly
		quarter.toss();
		if (quarter.getSideUp() == "heads")
			balance += 0.25;
		dime.toss();
		if (dime.getSideUp() == "heads")
			balance += 0.10;
		nickle.toss();
		if (nickle.getSideUp() == "heads")
			balance += 0.05;
		//2.2 Print the output of each toss and the balance after each toss
		cout << "Quarter: " << quarter.getSideUp() << ", Dime: " << dime.getSideUp() 
			<< ", Nickle: " << nickle.getSideUp() << endl;
		cout << "Balance: " << balance << endl;
	}

	//3. Determine if the user won the game by testing if balance is equal to 1 or not and print the result
	if (balance == 1.0)
		cout << "Game Result: You win\n";
	else
		cout << "Game Result: You lose\n";
	return 0;
}
