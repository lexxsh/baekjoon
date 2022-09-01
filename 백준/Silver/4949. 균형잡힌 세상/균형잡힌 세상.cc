#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (1) {
        stack<int> st;
        string str;
        getline(cin, str);
        if (str == ".") break;
        bool ans = true;
        for (auto c : str) {
            if (c == '(' || c == '[') st.push(c);
            else if (c == ')') {
                if (st.empty() || st.top() != '(') {
                    ans = false;
                    break;
                }
                st.pop();
            }
            else if (c == ']') {
                if (st.empty() || st.top() != '[') {
                    ans = false;
                    break;
                }
                st.pop();
            }
        }
        if (!st.empty()) ans = false;
        if (ans) cout << "yes"<<"\n";
        else cout << "no"<<"\n";
    }
}   