#include<bits/stdc++.h>
using namespace std;
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int a,cnt,b(3);
  string res = "EABCD";
  while(b--){
    cnt = 0;
    for(int i=0;i<4;i++){
      cin>>a;
      if(a == 0) cnt ++;
    }
    cout << res[cnt]<<"\n";
  }
}