#pragma once
//Odometer.h
#ifndef ODOMETER_H
#define ODOMETER_H
#include <iostream>
#include "FuelGauge.h"
class Odometer {
private:
	int mileage; //total mileage on vehicle
	int addedMiles; //miles drives since the object was declared
public:
	Odometer(int miles) //constructor initializes mileage and addedMiles
	{
		mileage = miles;
		addedMiles = 0;
	}

	void report() //reports number of miles
	{
		std::cout << "Mileage: " << mileage << std::endl;
	}

	void advance(int miles, FuelGauge& obj) //adds miles to the vehicles, and regulates fuel economy
	{
		if (mileage != 999999)
			mileage++;
		else
			mileage = 0;
		addedMiles++;
		if (addedMiles == 24) //if the vehicle has driven 24 miles, it loses one gallon
		{
			obj.gallons -= 1;
			addedMiles = 0;
		}
	}
};
#endif // ODOMETER_H