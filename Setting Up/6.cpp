// swapping two numbers without using the third variable
#include <iostream>
using namespace std;

int main()
{
    int first = 0, second = 0;
    cout << "Enter the first number: ";
    cin >> first;
    cout << "Enter the second number: ";
    cin >> second;

    first = first + second;
    second = first - second;
    first = first - second;

    cout << "After swapping: " << endl;
    cout << "First number: " << first << endl;
    cout << "Second number: " << second;

    cout << endl;
    return 0;
}