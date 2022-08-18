#include<bits/stdc++.h>
using namespace std;
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  int ans[26]={};
  cin>>s;
  for(int i = 0;i<s.size();i++){
    ans[s[i]-'a']++;
  }
  for(int e : ans){
    cout<<e<<' ';
  }
}
