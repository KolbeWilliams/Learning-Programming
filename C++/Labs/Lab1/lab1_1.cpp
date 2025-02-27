/*#include <iostream>
#include "Car.h"
using namespace std;

int main()
{
	//1. Create an object of Car class
	Car c1(1965, "Buick");

	//2. Print c1 data
	cout << "Data from this car: " << c1.getYear() << ", " << c1.getMake() << endl;

	//3. Use a for loop to call accelerate method five times and print the speed
	for (int i = 0; i < 5; i++)
	{
		c1.accelerate();
		cout << "Current speed: " << c1.getSpeed() << endl;
	}
	
	//4. Use a for loop to call brake method five times and print the speed
	for (int i = 0; i < 5; i++)
	{
		c1.brake();
		cout << "Current Speed: " << c1.getSpeed() << endl;
	}

	return 0;
}*/