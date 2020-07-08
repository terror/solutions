#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, a = 0, b = 0;
int ar[mxN];

int main()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> ar[i];

    sort(ar, ar + n, greater<int>());
    for (int i = 0; i < n; ++i)
        if (i % 2 == 0)
            a += ar[i];
        else
            b += ar[i];

    cout << a << ' ' << b;
    return 0;
}