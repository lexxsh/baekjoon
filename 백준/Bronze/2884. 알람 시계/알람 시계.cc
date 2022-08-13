#include<stdio.h>
int main(void) {
	int h, s;
	scanf("%d %d", &h, &s);
	if (s < 45) {
		s += 15;
		h--;
	}
	else s -= 45;
	if (h < 0) h += 24;
	printf("%d %d", h, s);
	return 0;
}