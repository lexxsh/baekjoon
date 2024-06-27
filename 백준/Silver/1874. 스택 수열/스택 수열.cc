#include<stack>
#include<iostream>
using namespace std;

int main() {
	stack<int> s1;
	int n;
	cin >> n;
	int k;
	int num = 1;
	string ans;
	while (n--) {
		cin >> k;
		while (num <= k) {
			s1.push(num);
			num++;
			ans += "+";
		}
		if (k == s1.top()) {
			s1.pop();
			ans += "-";
		}
		else {
			cout << "NO";
			return 0;
		}
	}
	for (auto a : ans) cout << a << "\n";
}
