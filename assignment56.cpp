//Stephanie Bravo
//April 10,2019
/*This program will ask the user for a number and draws a grid of
zeros and ones of that height and width using 'character graphics'*/

#include <iostream>
using namespace std;

int main()
{
  int i,j,numero;
  cout << "Enter a number: ";
  cin >> numero;
  for (i = 0; i <=numero; i++)
  {
    for (j = 0; j < i; j++)
      cout << "*";
    cout << endl;
  }
  return 0;
}
