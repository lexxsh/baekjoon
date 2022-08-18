#include<bits/stdc++.h>
using namespace std;
  int ans[26];
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin>>s;
  for(auto e : s) ans[e-'a']++;
  for(auto e : ans) cout<<e<<' ';
}