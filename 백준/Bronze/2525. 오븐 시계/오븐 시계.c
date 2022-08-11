#include<stdio.h>

int main(void) {
	int h, m, c;
	scanf("%d %d %d", &h, &m, &c);
	m += c;
	if (m > 59) {
		h += m / 60;
		m %= 60;
	}
	h %= 24;
	printf("%d %d", h, m);
}