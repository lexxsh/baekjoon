#include<queue>
#include<iostream>

using namespace std;

int main() {
	queue<int> q;
	int n;
	int ans;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	while (q.size()!=1) {
		q.pop();
		q.push(q.front());
		q.pop();
	}
	cout << q.front();}