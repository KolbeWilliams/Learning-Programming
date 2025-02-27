/*#pragma once
//Car.h
//DO NOT MODIFY THIS SECTION
#ifndef CAR_H
#define CAR_H
#include <string>
class Car
{
private:
	int year;
	std::string make;
	int speed;
public:
	Car(int y, std::string m);
	int getYear();
	//ADD YOUR CODE FROM HERE
	//Add prototypes for accessors and accelerate and brake methods
	std::string getMake() const;
	int getSpeed() const;
	int accelerate();
	int brake();
};
#endif*/