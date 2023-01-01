#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    vector<string> listOfString{"Hello", "World", "Welcome", "To", "World", "of", "C++", "Programming"};

    for (string &word : listOfString)
    {
        cout << word << " ";
    }

    cout << endl;
    return 0;
}