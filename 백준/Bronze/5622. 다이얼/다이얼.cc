#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int a[]={3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};
  int sum(0);
  string s;
  cin>>s;
  for(auto c : s){
    sum += a[c-'A'];
  }
  cout<<sum;
}