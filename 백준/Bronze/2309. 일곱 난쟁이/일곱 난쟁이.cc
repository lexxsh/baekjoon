#include<bits/stdc++.h>
using namespace std;
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int a[9],result[2],sum(0);
  for(int i = 0;i<9;i++){
    cin>>a[i];
    sum+=a[i];
  }
  sort(a,a+9);
  for(int i =0;i<8;i++){
    for(int j= i+1;j<9;j++){
      if(a[i]+a[j]==sum-100) {
        result[0]=a[i];
        result[1]=a[j];
      }
    }
  }
  for(int i = 0;i<9;i++){
    if(a[i]==result[0] || a[i] ==result[1]) continue;
    else cout  << a[i]<<"\n";
  }
}