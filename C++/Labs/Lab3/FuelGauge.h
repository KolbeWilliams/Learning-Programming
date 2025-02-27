#pragma once
//FuelGauge.h
#ifndef FUELGAUGE_H
#define FUELGAUGE_H
#include <iostream>
class FuelGauge {
private:
	int gallons; //gallons in the tank
public:
	friend class Odometer;

	FuelGauge(int gals) //constructor initializes gallons member
	{
		gallons = gals;
	}

	int getGallons() //getter method for gallons member
	{ return gallons; }

	void report() //reports the number of gallons and if the tank is empty
	{
		if (gallons == 0)
			std::cout << "Fuel: " << gallons << "\nEMPTY!\n";
		else
			std::cout << "Fuel: " << gallons << std::endl;
	}

	void addToTank(int gal) //adds gallons to tank up to 15 gallons
	{
		if (gallons <= 14 && gallons + gal <= 15)
		{
			std::cout << "Adding fuel, going from " << gallons << " to " << gallons + 1 << std::endl;
			gallons += 1;
		}
		else if (gallons + gal > 15)
		{
			std::cout << "Adding fuel, going from " << gallons << " to 15\n";
			gallons = 15;
		}
		else
		{
			std::cout << "Tank is full, cannot add any more!\n";
		}
	}
};
#endif // FUELGAUGE_H