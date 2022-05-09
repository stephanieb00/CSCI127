//Stephanie Bravo
//April 11, 2019
//This program will ask someone for their age until it is a positve number
#include <iostream>
using namespace std;

int main()
{
  //enter age
  int age;
  cout << "Please enter age: ";
  cin >> age;
  while (age<0) {
    cout << "Entered a negative number." << '\n';
    cout << "Please enter age: ";
    cin >> age;
  }
  cout << "You entered your age as: "<< age;
  return 0;
}
