// find Size of fundamental data types
#include <iostream>
using namespace std;

int main()
{
    bool temp = sizeof(long) == sizeof(int32_t);
    cout << "Size of char is: " << sizeof(char) << endl;
    cout << "Size of short is: " << sizeof(short) << endl;
    cout << "Size of int is: " << sizeof(int) << endl;
    cout << "Size of long is: " << sizeof(long) <<" - "<< sizeof(int64_t) << endl;
    cout << "Size of long long is: " << sizeof(long long) << endl;
    cout << "Size of float is: " << sizeof(float) << endl;
    cout << "Size of double is: " << sizeof(double) << endl;
    cout << "Size of long double is: " << sizeof(long double) << endl;
    cout << "Size of bool is: " << sizeof(bool) << endl;
    cout << endl;
}