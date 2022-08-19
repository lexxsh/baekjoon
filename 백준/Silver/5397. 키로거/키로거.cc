#include<bits/stdc++.h>
using namespace std;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin>>n;
  while(n--){
    string m;
    cin>>m;
    list<char> L;
    auto cuser = L.begin();
    for(auto c : m){
      if(c=='<'){
        if(cuser != L.begin()) cuser--;
      }
      else if(c=='>'){
        if(cuser != L.end()) cuser++;
      }
      else if(c=='-'){
        if(cuser != L.begin()){
          cuser--;
          cuser = L.erase(cuser);
        }  
      }
      else L.insert(cuser,c);
    }
    for(auto c : L) cout << c ;
    cout<<"\n";
  }
}
