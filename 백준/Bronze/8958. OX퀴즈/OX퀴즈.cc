#include<stdio.h>
#include<string.h>
int main(void) {
	int n,sum,add;
	char g[80] = {};
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		sum = 0, add = 1;
		scanf("%s", g);
		for (int j = 0; j < strlen(g); j++) {
			if (g[j] == 'O') {
				sum += add;
				add++;
			}
			else add = 1;
		}
		printf("%d\n", sum);
	}
	return 0;
}