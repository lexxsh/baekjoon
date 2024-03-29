#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    deque<int> d;
    int n;
    cin >> n;
    while (n--) {
        string s;
        cin >> s;
        if (s == "push_front") {
            int k;
            cin >> k;
            d.push_front(k);
        }
        else if (s == "push_back") {
            int k;
            cin >> k;
            d.push_back(k);
        }
        else if (s == "pop_front") {
            if (d.empty()) cout << -1 << "\n";
            else {
                cout << d.front() << "\n";
                d.pop_front();
            }
        }
        else if (s == "pop_back") {
            if (d.empty()) cout << -1 << "\n";
            else {
                cout << d.back() << "\n";
                d.pop_back();
            }
        }
        else if (s == "size") {
            cout << d.size() << "\n";
        }
        else if (s == "empty") {
            cout << (int)d.empty() << "\n";
        }
        else if (s == "front") {
            if (d.empty()) cout << -1 << "\n";
            else cout << d.front() << "\n";
        }
        else if (s == "back") {
            if (d.empty()) cout << -1 << "\n";
            else cout << d.back() << "\n";
        }
    }
}