#include<bits/stdc++.h>
using namespace std;
int num[9];
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n,max(0);
  int set[10]={};
  cin>>n;
  while(n!=0){
    set[n%10]++;
    n/=10;
  }
  set[6] = (set[6]+set[9]+1)/2;
  set[9] = 0;
  for(auto c : set) if(max < c) max = c;
  cout<< max;
}
