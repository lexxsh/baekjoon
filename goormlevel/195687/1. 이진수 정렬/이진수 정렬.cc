#include <iostream>
#include<algorithm>
using namespace std;
int a[500000];

int binary(int n) {
	int cnt = 0;
	while (n) {
		if (n % 2 == 1)
			cnt++;
		n/=2;
	}
	return cnt;
}

int compare(int a,int b){
	int one = binary(a);
	int one2 = binary(b);
	if(one == one2){
		return a < b;
	}
	return one < one2;
}
int main() {
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a,a+n,compare);
	cout << a[n-k];
	return 0;
}