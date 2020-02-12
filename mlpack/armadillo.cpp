#include<armadillo>
#include<iostream>

using namespace std;
using namespace arma;

int main(void)
{
  mat A = randu<mat>(1, 5);
  mat B = randu<mat>(1, 1);
  cout << A<<"\n";
  mat x = A + B;
  cout << x;
  return 0;
}
