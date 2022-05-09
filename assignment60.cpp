//Stephanie Bravo
//May 1,2019
//This program will convert whole number to two complement

#include <iostream>
using namespace std;

int main() {
  int n,x,b;
  cout << "Enter a number: ";
  cin >> n;
  //If the number is negative, print a 1 and let x = 32 + n.
  if (n < 0) {
    cout << "1";
    x = 32+ n;
  }
  //If the number is not negative, print a 0 and let x = n.
  else{
    cout << "0";
    x = n;
  }
  b = 16;
  //While b > 0.5:
  while (b > 0.5 ) {
    //If x >= b then print 1, otherwise print 0
    if (x>=b) {
      cout << "1";
    }
    else{
      cout << "0";
    }
    //Let x be the remainder of dividing x by b.
    x = x % b;
    //Let b be b/2.
    b = b/2;
  }
  //Print a new line ('\n').
  cout << '\n';


  return 0;
}
