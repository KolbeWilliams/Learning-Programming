//DO NOT MODIFY THIS SECTION
/*#include <iostream>
#include <iomanip>

using namespace std;

int main()

{
    int calories, fatGrams, fatCalories;
    float fatPercent;
    //1. Input data
    do {
        cout << "How many calories? ";
        cin >> calories;
    } while (calories < 0);
    //ADD YOUR CODE FROM HERE
    cout << "How many fat grams? ";
    cin >> fatGrams;

    //2. Calculate
    fatCalories = fatGrams * 9;
    if (fatCalories > calories)
    {
        cout << "The number of calories or fat grams were entered incorrectly." << endl;
        return 0;
    }
    fatPercent = static_cast<float>(fatCalories) / calories * 100;

    //3. Display results
    cout << "Fat percent is: " << fatPercent << "%" << endl;
    if (fatPercent < 30)
        cout << "This food is low in fat." << endl;
    return 0;
}*/