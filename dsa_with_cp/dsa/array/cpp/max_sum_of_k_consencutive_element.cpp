#include <iostream>
using namespace std;

int max_sum_of_k_consencutive_element(int arr[], int n, int k) {
    int max_sum = 0;
    for (int i = 0; i + k - 1 < n; i++) {
        int sum = 0;
        for (int j = 0; j < k; j++) {
            sum += arr[i + j];
        }
        max_sum = max(max_sum, sum);
    }

    return max_sum;
}

int main() {
    int arr[] = {1, 2 ,5, 77, 22, 51}, k = 3, n = 6;
    cout<<max_sum_of_k_consencutive_element(arr, n, k)<<endl;
}
