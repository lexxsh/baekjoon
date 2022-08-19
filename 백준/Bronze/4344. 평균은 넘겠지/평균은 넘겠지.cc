#include<bits/stdc++.h>
using namespace std;
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int c,n,score[1000];
  cin>>c;
  for(int i = 0;i<c;i++){
    int avg(0),cnt(0);
    double ans;
    cin >> n;
    for(int j = 0;j<n;j++){
      cin >> score[j];
      avg+=score[j];
    }
    avg /=n;
    for(int j = 0;j<n;j++){
      if(score[j]>avg) cnt++;
    }
    ans = (double)cnt/n*100;
    cout << fixed;
    cout.precision(3);
    cout<<ans<<"%"<<"\n";
  }
}