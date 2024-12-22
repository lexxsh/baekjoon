#include<stdio.h>
int main(void) {
	int n;
	int k = 2;
	int o = 5;
	int cnt = 2;
	scanf("%d", &n);
	if (n == 1) {
		printf("1");
		return 0;
	}
	while (1) {
		if (k <= n && n <= k+o) {
			printf("%d", cnt);
			break;
		}
		k += o + 1;
		o += 6;
		cnt++;
	}
}