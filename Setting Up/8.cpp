// get a string input
#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int main()
{
    string itAString;
    cout << "Enter a string: ";
    getline(cin,itAString);

    cout << "Length of the string is: " << itAString.length() << endl;
    reverse(itAString.begin(), itAString.end());
    cout << "Reverse of a string:" << itAString << endl;

    cout << "Reversing a reversed string:" << string(itAString.rbegin(), itAString.rend()) << endl;
    return 0;
}