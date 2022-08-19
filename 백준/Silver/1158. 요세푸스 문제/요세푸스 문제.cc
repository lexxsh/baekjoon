#include<bits/stdc++.h>
using namespace std;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n,k;
  
  cin>>n>>k;
  list<int> L;
  list<int>::iterator cur;
  for(int i = 1;i<=n;i++) L.push_back(i);
  cur = L.begin();
  cout<<'<';
  while(L.size()>1){
    for(int i =0;i<k-1;i++){
      cur++;
      if(cur == L.end()) {
        cur = L.begin();
      }
    }
    cout << *cur << ", ";
    cur = L.erase(cur);
    if(cur == L.end()) {
      cur = L.begin();
    }
  }
  cout<<*cur<<'>';
}