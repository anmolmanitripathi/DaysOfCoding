// pre and post increment/decrement
#include <iostream>
using namespace std;

int main()
{
    int i = 0;

    cout << "Value of i: " << i << endl;
    cout << "Pre-increment: " << ++i << endl;
    cout << "Value of i: " << i << endl;
    cout << "Post-increment: " << i++ << endl;
    cout << "Value of i: " << i << endl;

    cout << "Hence post increment means it does the work and then increments the value" << endl;
    cout << "and pre increment means that it increments the value first and then does the work";

    cout << endl;
    return 0;
}