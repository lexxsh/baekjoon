#include<stdio.h>
int main(void) {
	int n;
	float score[1000];
	int max = 0;
	float avr = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%f", &score[i]);
		if (score[i] > max) max = score[i];
	}
	for (int i = 0; i < n; i++) {
		score[i] = (score[i] / max * 100);
		avr += score[i];
	}
	printf("%.2f", avr / n);
}