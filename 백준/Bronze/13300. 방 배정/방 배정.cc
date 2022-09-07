#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k, score(0);
    int stu[2][6] = {};
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        int s, y;
        cin >> s >> y;
        stu[s][y-1]++;
    }
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 6; j++) {
            score += stu[i][j] / k;
            if (stu[i][j] % k ) score++;
        }
    }
    cout << score;
}
