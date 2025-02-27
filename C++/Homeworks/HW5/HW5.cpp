//DO NOT MODIFY THIS SECTION
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//prototypes
void modify1();
void modify2();
void modify3();
void displayData();
void save();

//globals
int age1, age2, age3, option = 0;
string name1, name2, name3;
ifstream ifile;
ofstream ofile;
bool saved;

int main()
{
    ifile.open("students.txt");
    //ADD YOUR CODE FROM HERE, INCLUDE YOUR FUNCTIONS
	//1. Read info
	ifile >> age1;
	getline(ifile, name1);
	ifile >> age2;
	getline(ifile, name2);
	ifile >> age3;
	getline(ifile, name3);

	//2.Close File
	ifile.close();
	saved = false;

	//3.Repeat while not leaving
	while (saved == false)
	{
		//3.1 Display Menu
		cout << "1. Display, 2. Mod First, 3. Mod Second, 4. Mod Third, 5. Save, 6. Quit" << endl;
		//3.2 Request Option
		cin >> option;
		//3.3 Switch Case
		switch (option)
		{
			//3.3.1 Case 1, display data
		case 1:
			displayData();
			break;
			//3.3.2 Case 2, modify first student
		case 2:
			modify1();
			break;
			//3.3.3 Case 3, modify second student
		case 3:
			modify2();
			break;
			//3.3.4 Case 4, modify third student
		case 4:
			modify3();
			break;
			//3.3.5 Case 5, Save information
		case 5:
			save();
			break;
			//3.3.6 Case 6, Quit
		case 6:
			return 0;
		}
	}
	return 0;
}

//4. Define functions
void modify1()
{
	cout << "Enter age1: ";
	cin >> age1;
	cout << "Enter name1: ";
	cin.ignore();
	getline(cin, name1);
}

void modify2()
{
	cout << "Enter age2: ";
	cin >> age2;
	cout << "Enter name2: ";
	cin.ignore();
	getline(cin, name2);
}

void modify3()
{
	cout << "Enter age3: ";
	cin >> age3;
	cout << "Enter name3: ";
	cin.ignore();
	getline(cin, name3);
}

void displayData()
{
	cout << age1 << " " << name1 << endl << age2 << " " << name2 << endl << age3 << " "
		<< name3 << endl << endl;
}

void save()
{
	ofile.open("students.txt");
	ofile << age1 << " " << name1 << endl << age2 << " " << name2 << endl << age3 << " "
		<< name3 << endl;
	ofile.close();
}