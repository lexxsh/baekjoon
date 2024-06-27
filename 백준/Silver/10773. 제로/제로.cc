#include<bits/stdc++.h>

using namespace std;

int main() {
	int k, sum(0);
	cin >> k;
	stack<int> s;
	while (k--) {
		int o;
		cin >> o;
		if (o == 0) {
			sum -= s.top();
			s.pop();
		}
		else {
			s.push(o);
			sum += o;
		}
	}
	cout << sum;
}