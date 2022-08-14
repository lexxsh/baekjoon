#include<iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, x;
    int num[10000];
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
        cin >> num[i];
    }
    for (int i = 0; i < n; i++) {
        if (num[i] < x) cout << num[i] << ' ';
    }
    return 0;
}