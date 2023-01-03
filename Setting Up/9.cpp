// swap first and last digits of any number
#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <math.h>
using namespace std;

int main()
{
    int i;
    cout << "Enter a number : ";
    cin >> i; 

    cout << "Using string -- " << endl;
    string numberInString = to_string(i);

    cout << "Character at the first = " << numberInString.front() << endl;
    cout << "Character at the last = " << numberInString.back() << endl;

    cout << "Older number is: " << i << endl;
    string newNumberInString = numberInString.back() + numberInString.substr(1, numberInString.length() - 2) + numberInString.front();
    int ri = stoi(newNumberInString);
    cout << "New number is: " << ri << endl;

    cout << "Using Maths -- " << endl;
    int digits = (int)log10(i) + 1;
    int lastDigit = i % 10;
    int firstDigit = i / pow(10, digits);

    int reverseNumber = i - (firstDigit * pow(10, digits)) + (lastDigit * pow(10, digits)) - lastDigit + firstDigit;
    cout << "New reversed number using maths is: " << reverseNumber << endl;

    cout << endl;
    return 0;
}