#include <iostream>
using namespace std;
void insertion_sort(int list[], int n){
  int i, j, key;
  for(i=1; i<n; i++){
    key = list[i];
    for(j=i-1; j>=0 && list[j]>key; j--){
      list[j+1] = list[j]; 
    }
    list[j+1] = key;
  }
}

int main() {
	int n;
	int k[100000];
	cin >> n;
	for (int i = 0;i<n;i++){
		cin >> k[i];
	}
	insertion_sort(k,n);
	for (int i = 0;i<n;i++){
		if(i>0 && k[i-1]==k[i])
			continue;
		cout << k[i] << " ";
	}
	return 0;
}