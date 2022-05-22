#include <iostream>
#include <cmath>
using namespace std;

void reverse(int arr[], int n) {
    int low = 0, high = n - 1;

    while (low < high) {
        /* code */
        int temp = arr[low];
        arr[low] = arr[high];
        arr[high] = temp;

        low++;
        high--;
    }
    
}

int main() {
    int arr[] = {2, 4, 5, 7}, n = 4;

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    cout<<endl;
    reverse(arr, n);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}
