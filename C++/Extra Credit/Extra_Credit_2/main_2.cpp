#include <iostream>

using namespace std;

int objNum = 0; //global variable used to keep up with object number

class Test
{
public:
	int obj; //object number for easily understandable output
	Test() //constructor
	{
		++objNum;
		obj = objNum;
		display();
	}
	void display()
	{
		cout << "Object " << obj << " Created\n";
	}
	~Test() //destructor
	{
		cout << "Object " << obj << " Destroyed\n";
	}
};

void functionThree() //creates an object and then throws an exception
{
	cout << "Function Three started\n";
	Test obj;
	cout << "Throwing exception inside function three...\n";
	throw 1;
}

void functionTwo() //creates an object and calls functionThree
{
	cout << "Function two started\n";
	Test obj;
	functionThree();
	cout << "FunctionTwo ended\n"; //This will never execute
}

void functionOne() //creates an object and calls functionTwo
{
	cout << "Function one started.\n";
	Test obj;
	functionTwo();
	cout << "Function one ended\n"; //This will never execute
}

int main()
{
	try
	{
		/*functionOne is called inside the try block, which creates object 1 and calls
		functionTwo. Then, functionTwo creates object 2 and calls functionThree. functionThree
		then creates object three and throws and exception. When the exception is thrown, the
		stack unwinds and the obects are destroyed in the reverse order from what they were
		created in.*/
		functionOne();
	}
	catch (int x)
	{
		cout << "Exception caught\n"; /*This executes when the exception is caught after the
		stack unwinds*/
	}
	return 0;
}