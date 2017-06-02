#include <iostream>
#include <string>
using namespace std;

int main() {
   // Complete the program
  string a;
  cin>>a;
  string b;
  cin>>b;
  cout<<a.size()<<" "<<b.size()<<endl;
  string a2,b2;
  a2=a;
  b2=b;
  a2[0]=b[0];
  b2[0]=a[0];
  cout<<a+b<<endl;
  cout<<a2<<" "<<b2<<endl;
    return 0;
}

