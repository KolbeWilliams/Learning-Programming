#include "Coin.h"
#include <iostream>
#include <ctime>
using namespace std;

void Coin::toss()
{
	//1. Generate a random number that is either 0 or 1
	int num = rand() % 2;
	
	//2. Set sideup member variable to either heads or tails depending on the random number 
	if (num == 0)
		Coin::sideup = "heads";
	else
		Coin::sideup = "tails";
}