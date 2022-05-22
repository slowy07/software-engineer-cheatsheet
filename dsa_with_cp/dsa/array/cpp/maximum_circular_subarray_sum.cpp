#include <iostream>
using namespace std;

int maxCircularSubarraySum(int arr[], int n) {
    int res = arr[0];
    for (int i = 0; i < n; i++) {
        int cur_max = arr[i];
        int cur_sum = arr[i];
        
        for (int j = 1; j < n; j++) {
            int index = (i + j) % n;
            cur_sum += arr[index];
            cur_max = max(cur_max, cur_sum);
        }
        res = max(res, cur_max);
    }
    return res;
}

int main() {
    int arr[] = {5, -2, 3, 28}, n = 4;
    cout<<maxCircularSubarraySum(arr, n)<<endl;
}
