#include <iostream>
using ll = long long;
using namespace std;

long long num_substrings(long long length,long long minimum){
    long long ans = 0;
    if (minimum > length){
        return 0;
    }
    for (long long substring = minimum; substring < length+1; substring++){
        //printf("%d %d %d \n",length,substring,length-(substring-1));
        ans += length-(substring-1);
    }
    return ans;
}

int main(){
    long long testcases,n,k;
    long long temp;
    long long q;
    cin >> testcases;

    for (long long t = 0; t < testcases; t++){
        cin >> n >> k >> q;
        long long ans = 0;
        long long consecutive = 0;
        for (long long x = 0; x < n; x++){
            cin >> temp;
            //printf("TEMP: %d \n",temp);
            if (temp <= q){
                consecutive++;
            } else {
                //printf("CONSECUTIVE %d \n",consecutive);
                ans += num_substrings(consecutive,k);
                consecutive = 0;
            }
        }
        if (consecutive != 0){
            ans += num_substrings(consecutive,k);
        }
        printf("%d \n",ans);
    }
}