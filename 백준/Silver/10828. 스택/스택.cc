#include <iostream>
#include <stack>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    stack<int> c;
    while (n--) {
        string s;
        cin >> s;
        if (s == "push") {
            int k;
            cin >> k;
            c.push(k);
        }
        else if (s == "pop") {
            if (c.empty()) cout << -1 << '\n';
            else {
                cout << (int)c.top() << '\n';
                c.pop();
            }
        }
        else if (s == "size") {
            cout << c.size() << '\n';
        }
        else if (s == "empty") {
            cout << c.empty() << '\n';
        }
        else if (s == "top") {
            if (c.empty()) cout << -1 << '\n';
            else cout << (int)c.top() << '\n';
        }
    }
}