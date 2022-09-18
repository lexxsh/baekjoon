#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    while (n--) {
        stack<char> s;
        string g;
        cin >> g;
        bool at = true;
        for (auto c : g) {
            if (c == '(') s.push(c);
            else {
                if (s.empty() || s.top() == ')') {
                    at = false;
                    break;
                }
                else s.pop();
            }
        }
        if (at && s.empty()) cout << "YES\n";
        else cout << "NO\n";
    }
}