#include<stdio.h>

int main(void) {
	int a[9];
	int max = 0;
	int num = 0;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &a[i]);
		if (a[i] > max) {
			max = a[i];
			num = i + 1;
		}
	}
	printf("%d\n%d", max, num);
}