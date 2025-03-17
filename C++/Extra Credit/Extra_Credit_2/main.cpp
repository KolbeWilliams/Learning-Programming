#include <iostream>

using namespace std;

class Divide
{
private:
	double a;
	double b;
	double c;
public:
	Divide() //constructor
	{
		a = 1.0;
		b = 1.0;
		c = 1.0;
	}
	double getA()
	{ return a; }
	double getB()
	{ return b; }
	void setA(int num)
	{ a = num; }
	void setB(int num)
	{ b = num; }
	double calculate()
	{ c = a / b; }
	~Divide() //Destructor is called when the object is destroyed and prints the message
	{
		cout << "Object Destroyed...\n";
	}
};

int main()
{
	double a, b;
	cout << "Enter two numbers seperated by a space to divide them:";
	cin >> a >> b;
	try 
	{
		Divide ans; //object created in the try block
		ans.setA(a);
		ans.setB(b);
		if (b == 0)
			throw "ERROR: cannot divide by zero.\n"; //The destructor message will execute
		//before the error message if the ans object is destroyed when the exception is thrown
		int c = a / b;
		cout << a << " / " << b << " = " << c << endl; //This will only be displayed if no 
		//exception is thrown
	}
	catch (const char* msg)
	{
		cout << msg;
	}
	return 0;
}