#include<iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, cycle(0), num;
    cin >> n;
    num = n;
    while (1) {
        cycle++;
        n = ((n / 10 + n % 10) % 10) + (n % 10) * 10;
        if (n == num) break;
    }
    cout << cycle;
}