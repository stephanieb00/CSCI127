//Stephanie Bravo
//April 11,2019
//This program asks the user for the starting amount, and prints out the yearly balance of a savings account, assuming 10% interest, until the amount has doubled.

#include <iostream>
using namespace std;

int main()
{
    float amount, b, i;
    cout << "Please enter the starting amount: ";
    cin >> amount;
    i=0;
    b = float(amount);
    //while the balance is less than twice the initial amount.
    while (b < (amount*2))
    {
      i ++;
      b = b +( b * 0.10);
      cout << "Year " << i <<" " << b <<'\n';
    }
  return 0;
}
