#include <iostream>
using namespace std;

class Employee
{
private:
	string employeeName, hireDate;
	int number;
public:
	Employee(string name, int num, string date) //Constructor
	{
		employeeName = name;
		number = num;
		hireDate = date;
	}

	void print() //Print function prints member fields
	{
		cout << "Name:      " << employeeName << endl;
		cout << "Number:    " << number << endl;
		cout << "Hire Date: " << hireDate << endl;
	}

	void setEmployeeName(string name) //Accessors and mutators for each field
	{ employeeName = name; }

	void setNumber(int num)
	{ number = num; }

	void setHireDate(string date)
	{ hireDate = date; }

	string getEmployeeName()
	{ return employeeName; }

	int getNumber()
	{ return number; }

	string getHireDate()
	{ return hireDate; }
};

class ProductionWorker : public Employee //Class is derived from Employee class
{
private:
	int shift;
	double hourlyPayRate;
public:
	//Constructor uses base class constructor
	ProductionWorker(string name, int num, string date, int shiftNum, double pay) : Employee(name, num, date)
	{
		shift = shiftNum;
		hourlyPayRate = pay;
	}

	void print() //Print function prints member fields
	{
		Employee::print();
		cout << " Position: Production Worker\n";
		cout << " Shift:    " << shift << endl;
		cout << " Pay rate: " << hourlyPayRate << endl;
	}

	void setShift(int shiftNum) //Accessors and mutators for each field
	{ shift = shiftNum; }

	void setHourlyPayRate(double pay)
	{ hourlyPayRate = pay; }

	int getShift()
	{ return shift; }

	double getHourlyPayRate()
	{ return hourlyPayRate; }
};

class ShiftSupervisor : public Employee //Class is derived from Employee class
{
private:
	int anualSalary, anualProductionBonus;
public:
	//Constructor uses base class constructor
	ShiftSupervisor(string name, int num, string date, int salary, int bonus) : Employee(name, num, date)
	{
		anualSalary = salary;
		anualProductionBonus = bonus;
	}
	
	void print() //Print function prints member fields
	{
		Employee::print();
		cout << " Position:     Shift Supervisor\n";
		cout << " Anual salary: " << anualSalary << endl;
		cout << " Anual bonus:  " << anualProductionBonus << endl;
	}

	void setAnualSalary(int salary) //Accessors and mutators for each field
	{ anualSalary = salary; }
	
	void setAnualProductionBonus(int bonus)
	{ anualProductionBonus = bonus; }
	
	int getAnaulSalary()
	{ return anualSalary; }
	
	int getAnaulProductionBonus()
	{ return anualProductionBonus; }
};

int main()
{
	ProductionWorker pw("Pete", 171, "Oct 2022", 1, 20.5);
	pw.print();
	cout << "---------" << endl;
	ShiftSupervisor ss("Micky", 112, "Feb 2018", 30000, 4000);
	ss.print();
	return 0;
}