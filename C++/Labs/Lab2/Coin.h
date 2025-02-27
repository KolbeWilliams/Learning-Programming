#pragma once
//Coin.h
//DO NOT MODIFY THIS SECTION
#ifndef COIN_H
#define COIN_H
#include <iostream>
class Coin {
private:
	std::string sideup;
public:
	Coin() //constructor
	{
		toss();
	}
	std::string getSideUp() //accesor
	{
		return sideup;
	}
	void toss();
};
#endif // COIN_H

