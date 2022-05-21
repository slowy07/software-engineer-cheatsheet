#include <iostream>
using namespace std;

int search(int arr[], int n, int x) {
    for(int i = 0; i < n; i++) {
        if (arr[i] == x)
            return i;
    }

    return -1;
}

int main() {
    int arr[] = {30, 50, 40, 5, 12, 222}, x= 12;
    cout<<"search index "<<search(arr, 4, x);
}