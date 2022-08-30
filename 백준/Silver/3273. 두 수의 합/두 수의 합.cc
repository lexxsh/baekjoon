#include<bits/stdc++.h>
using namespace std;
int a[100001];
int b[2000001];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,x,cnt(0);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        b[a[i]]++;
    }
    cin >> x;
    for (int i = 0; i < n; i++) {
        if (x>a[i] && b[x - a[i]] == 1)cnt++;
    }
    cout << cnt/2;
}