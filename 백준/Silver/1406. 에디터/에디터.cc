#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string m;
    cin >> m;
    list<char> l;
    for (auto c : m) l.push_back(c);
    auto cuser = l.end();
    int k;
    cin >> k;
    while (k--) {
        char order;
        cin >> order;
        if (order == 'L') {
            if (cuser != l.begin()) cuser--;
        }
        else if (order == 'P') {
            char a;
            cin >> a;
            l.insert(cuser, a);
        }
        else if (order == 'D') {
            if (cuser != l.end()) cuser++;
        }
        else {
            if (cuser != l.begin()) {
                cuser--;
                cuser = l.erase(cuser);
            }
        }
    }
    for (auto c : l) cout << c;
}