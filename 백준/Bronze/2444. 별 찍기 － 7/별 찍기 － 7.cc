#include<bits/stdc++.h>
using namespace std;
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin>>n;
  for(int i =1;i<n;i++){
    for(int j =0;j<n-i;j++) cout<<" ";
    for(int j =1;j<i*2;j++) cout<<"*";
    cout<<"\n"; 
  }
  for(int i =0;i<n;i++){
    for(int j =0;j<i;j++) cout<<" ";
    for(int j =1;j<n*2-i*2;j++) cout<<"*";
    cout<<"\n"; 
  }
}