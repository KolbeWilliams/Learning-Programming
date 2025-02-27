/*#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	//1. Declare variables
	ifstream ifile;
	ofstream ofile;
	int age1, age2, age3;
	string name1, name2, name3;
	//2. Open file
	ifile.open("students.txt");
	if (!ifile)
	{
		cout << "Problem with the file" << endl;
		return 1;
	}
	//3. Read info from each student
	// 3.1 Read ages and names
	ifile >> age1;
	getline(ifile, name1);
	ifile >> age2;
	getline(ifile, name2);
	ifile >> age3;
	getline(ifile, name3);
	//4. Close the file
	ifile.close();
	bool leave = false;
	int option;
	//5. Repeat while not leaving
	while (leave == false)
	{
		// 5.1 Present the menu
		cout << "1. Display, 2. Mod First, 3. Mod Second, 4. Mod Third, 5. Save, 6. Quit" << endl;
		// 5.2 Request option
		cin >> option;
		// 5.3 Switch case
		switch (option)
		{
			// 5.3.1 Case 1, display data
		case 1:
			cout << age1 << " " << name1 << endl << age2 << " " << name2 << endl << age3 << " "
				<< name3 << endl << endl;
			break;
			// 5.3.2 Case 2, modify first student
		case 2:
			cout << "Enter age1: ";
			cin >> age1;
			cout << "Enter name1: ";
			cin.ignore();
			getline(cin, name1);
			break;
			// 5.3.3 Case 3, modify second student
		case 3:
			cout << "Enter age2: ";
			cin >> age1;
			cout << "Enter name2: ";
			cin.ignore();
			getline(cin, name2);
			break;
			// 5.3.4 Case 4, modify third student
		case 4:
			cout << "Enter age3: ";
			cin >> age1;
			cout << "Enter name3: ";
			cin.ignore();
			getline(cin, name3);
			break;
			// 5.3.5 Case 5,Save information
		case 5:
			ofile.open("students.txt");
			ofile << age1 << " " << name1 << endl << age2 << " " << name2 << endl << age3 << " "
				<< name3 << endl;
			ofile.close();
			break;
			// 5.3.6 Quit
		case 6:
			return 0;
		}
	}
	return 0;
}*/