//Stephanie Bravo
//April 10, 2019
//This program will greet people based on the time they Enter


//"Good Morning" if it is strictly before 12,
//"Good Afternoon" if it is 12 or greater, but strictly before 17, and
//"Good Evening" otherwise.
#include <iostream>
using namespace std;

int main()
{
  int hora;
  cout << "Enter hour (in 24 hour time): ";
  cin >> hora;
  //if it is strictly before 12: Good Morning
  if (hora < 12) {
    cout << "Good Morning";
  }
  else if(hora >= 12 and hora <17){
    cout << "Good Afternoon";
  }
  else{
    cout << "Good Evening";
  }
  return 0;
}
