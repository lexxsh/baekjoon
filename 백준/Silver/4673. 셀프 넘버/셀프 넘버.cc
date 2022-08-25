#include<bits/stdc++.h>

using namespace std;
bool a[10001];

void check(int num){
	int sum = num;
	while (num) {
		sum += num % 10;
		num /= 10;
	}
	a[sum] = true;
}
int main() {
	for (int i = 0; i < 10000; i++) {
		check(i);
	}

	for (int i = 0; i < 10001; i++) {
		if (a[i] == false) cout << i << '\n';
	}
}