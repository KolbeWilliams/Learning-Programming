#include <iostream>
#include "Coin.h"
using namespace std;

int main()
{
	srand(time(nullptr));

	//1. Create an object of the Coin class
	Coin c1;

	//2. Declare and initialize heads and tails count variables
	int heads = 0, tails = 0;

	//3. Print begininng string value of sideup member variable
	cout << c1.getSideUp() << endl;

	//4. Use a for loop to toss the coin 20 times and record the number of heads and tails
	for (int i = 0; i < 20; i++)
	{
		c1.toss();
		if (c1.getSideUp().compare("heads") == 0)
			heads++;
		else
			tails++;
		cout << c1.getSideUp() << endl;
	}

	//5. Display the results
	cout << "Heads: " << heads << endl;
	cout << "Tails: " << tails << endl;
	return 0;
}