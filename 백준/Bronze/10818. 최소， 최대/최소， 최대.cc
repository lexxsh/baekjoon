#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n,k[1000000];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> k[i];
    }
    cout <<*min_element(k, k + n)<< ' '<< *max_element(k,k+n)  ;
}