#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    int n, x;
    cin >> n >> x;

    int a[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    sort(a, a + n);
    int i = 0;
    int j = n - 1;

    while (i < j)
    {
        while (a[i] + a[j] > x)
        {
            --j;
        }
        if (i >= j)
            break;
        n--;
        ++i, --j;
    }

    cout << n;
    return 0;
}