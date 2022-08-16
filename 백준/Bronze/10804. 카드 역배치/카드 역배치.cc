#include<iostream>
#include<math.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a, b, n[21];
    for (int i = 1; i <= 20; i++) n[i] = i;
    for (int i = 1; i <= 10; i++) {
        cin >> a >> b;
        for (int j = 0; j < (b - a + 1) / 2; j++) {
            swap(n[a + j], n[b - j]);
        }
    }
    for (int i = 1; i <= 20; i++) cout << n[i] << ' ';
}
