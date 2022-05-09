//Stephanie Bravo
//April 10,2019
//This program will convert kilometers to miles

#include <iostream>
using namespace std;

int main()
{
  //telling the computer kilo is a float
  float kilo;
  float miles;
  //input for kilo
  cin>> kilo;
  //miles = 0.621371* kilometers.
  miles = 0.621371 * kilo;
  //print the number of miles
  cout << miles << '\n';
  return 0;
}
