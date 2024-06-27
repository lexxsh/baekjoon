#include<bits/stdc++.h>

using namespace std;

int main() {
	int n,cnt(1);
	string k;
	cin >> n;
	stack<int>s;
	while (n--) {
		int x;
		cin >> x;
		while (cnt <= x) {
			s.push(cnt++);
			k += "+";
		}
		if (x == s.top()) {
			s.pop();
			k += "-";
		}
		else {
			cout << "NO";
			return 0;
		}
	}
	for (auto c : k) cout << c << '\n';
}