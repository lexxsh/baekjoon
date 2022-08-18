#include<stdio.h>

int main(void) {
	int a, b, c;
	int k[10] = {};
	scanf("%d %d %d", &a, &b, &c);
	int an = a * b * c;
	while (an != 0) {
		k[an % 10]++;
		an /= 10;
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n", k[i]);
	}
}