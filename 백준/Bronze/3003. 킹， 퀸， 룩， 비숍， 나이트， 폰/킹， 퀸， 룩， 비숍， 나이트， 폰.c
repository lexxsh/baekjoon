#include<stdio.h>

int main(void) {
	int a[6] = { 1,1,2,2,2,8 };
	int b[6];
	for (int i = 0; i < 6; i++) {
		scanf("%d", &b[i]);
		printf("%d ", a[i] - b[i]);
	}
}