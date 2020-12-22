// Print elements of an array in alternatively sorted way

// Input

// 1, 12, 4, 6, 7, 10, 3

// Output

// 12 1 10 3 7 4 6

#include <bits/stdc++.h>
using namespace std;
int main() {
    int arr[] = {1, 12, 4, 6, 7, 10, 3};
    int le = sizeof(arr)/sizeof(arr[0]);
    int i = 0,j = le - 1;
    sort(arr, arr + le);
    // 1 3 4 6 7 10 12
    while(i<j) {
        cout<< arr[j]<<' ';
        j--;
        cout<< arr[i]<< ' ';
        i++;
    }
    if(le%2 != 0) {
        cout<< arr[i];
    }
}
