#include<iostream>
using namespace std;
int num[2000001];
int k[100001];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, x, cnt(0);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> k[i];
        num[k[i]]++;
    }
    cin >> x;
    for (int i = 0; i < n; i++) {
        if (x > k[i] && num[x - k[i]]) cnt++;
    }
    cout << cnt/2;
}