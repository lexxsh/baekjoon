#include<bits/stdc++.h>

using namespace std;
int cnt(0);
void check(int num) {
	int a1, a2, a3;
	if (num < 100) cnt++;
	else {
		a1 = num % 10;
		a2 = (num / 10) % 10;
		a3 = (num / 100);
		if ((a1 - a2) == (a2 - a3)) cnt++;
	}
}

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		check(i);
	}
	cout << cnt << '\n';
}