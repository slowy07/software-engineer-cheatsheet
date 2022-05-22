#include <iostream>
using namespace std;

int findMajority(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j])
                count++;
        }
        if (count > n / 2)
            return i;
    }
    return -1;
}

int main() {
    int arr[] = {2, 3, -8, 7, -1, 2, 3}, n = 7;
    cout<<findMajority(arr, n)<<endl;
}
