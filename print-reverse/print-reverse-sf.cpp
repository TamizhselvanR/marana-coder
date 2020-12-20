// Straight forward Approach

#include <bits/stdc++.h>
using namespace std;

int main()
{
    string ip;
    int i;
    vector <string> arr;
    while (cin >> ip) {
        arr.push_back(ip);
    }
    i = arr.size();
    while (i >= 0) {
        cout<<arr[i]<<" ";
        i--;
    }
}
