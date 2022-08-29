#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin >> n;
    string word;
    int ans = 0;
    for (int i = 0; i < n; i++){
        bool isgroup = true; // 그룹인지 확인하는 변수
        cin >> word;
        word.erase(unique(word.begin(), word.end()), word.end());
        //연속된 중복값 맨 뒤로 보내서 제거
 
        sort(word.begin(), word.end()); // 정렬
        for (int k = 0; k < word.length()-1;k++){
            if(word[k] == word[k+1]){//중복된값이 있으면
                isgroup = false; //그룹이 아님
                break;
            }
        }
        if(isgroup){
            ans++;
        }
    }
    cout << ans;
    return 0;
}