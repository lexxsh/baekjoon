#include<stdio.h>
#define max(x,y) ( (x) > (y) ? (x) : (y))
int main(void) {
	int a, b, c, score;
	scanf("%d %d %d", &a, &b, &c);
	if (a == b && b == c) printf("%d",10000 + a * 1000);
	else if (a == b || b == c) printf("%d",1000 + b * 100);
	else if (a == c) printf("%d",1000 + c * 100);
	else printf("%d",max(max(a, b), c)*100);
}