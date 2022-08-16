#include<bits/stdc++.h>
using namespace std;
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int x,n,a,b,sum(0);
  cin>>x>>n;
  for(int i =0;i<n;i++){
    cin >> a >> b;
    sum+=a*b;
  }
  if(sum == x) cout<<"Yes";
  else cout<<"No";
}