#include <iostream>
using namespace std;

int getLarger(int arr[], int n) {
    int larger = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > arr[larger]) {
            larger = i;
        }
    }
    return larger;
}

int getSecondLarger(int arr[], int n) {
    int larger = getLarger(arr, n);
    int res = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] != arr[larger]) {
            if (res == -1)
                res = i;
            else if (arr[i] > arr[res])
                res = i;
        }
    }
    return res;
}

int main() {
    int arr[5] = {5, 10, 20, 30, 40}, n = 5;
    cout<<getSecondLarger(arr, n)<<endl;
}
