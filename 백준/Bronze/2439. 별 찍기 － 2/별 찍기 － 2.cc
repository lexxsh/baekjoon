#include<stdio.h>
int main(void) {
	int a;
	scanf("%d", &a);
	for (int i = 1; i <= a; i++) {
		for (int j = a - i; j > 0; j--)printf(" ");
		for (int j = 0; j < i; j++)printf("*");
		printf("\n");
	}
}