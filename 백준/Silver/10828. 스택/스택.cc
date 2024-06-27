#include<stack>
#include<iostream>
using namespace std;

int main() {
	stack<int> s1;
	int n;
	string k;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num = 0;
		cin >> k;
		if (k == "push") {
			cin >> num;
			s1.push(num);
		}
		else if (k == "top") {
			if (s1.empty()) cout << "-1" << "\n";
			else cout << s1.top() << "\n";
		}
		else if (k == "size") cout << s1.size() << "\n";
		else if (k == "empty") cout << s1.empty() << "\n";
		else if (k == "pop") {
			if (s1.empty()) cout << "-1"<<"\n";
			else {
				cout << s1.top() << "\n";
				s1.pop();
			}
		}
	}

}