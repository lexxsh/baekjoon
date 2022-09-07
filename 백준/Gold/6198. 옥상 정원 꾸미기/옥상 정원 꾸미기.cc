#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<long long> s;
    long long n,cnt(0);
    long long h;
    cin >> n;
    while (n--) {
        cin >> h;
        while (!s.empty() && s.top() <= h) {
            s.pop();
        }
        cnt += s.size();
        s.push(h);
    }
    cout << cnt ;
}