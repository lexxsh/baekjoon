#include<bits/stdc++.h>
using namespace std;
int a[2][26];
int score;
string s, s1;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> s >> s1;
    for (char c : s) {
        a[0][c- 'a']++;
    }
    for (char c : s1) {
        a[1][c- 'a']++;
    }
    for (int i = 0; i < 26; i++) {
        score += abs(a[0][i] - a[1][i]);
    }
    cout << score;
}