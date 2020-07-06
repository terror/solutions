#include <bits/stdc++.h>

using namespace std;
const int mxN = 2e5;
int n, m;
int a[mxN], b[mxN];

int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < m; ++i)
        cin >> b[i];

    sort(a, a + n, greater<int>());
    sort(b, b + m, greater<int>());

    int ans = 0;
    for (int i = 0, j = 0; i < n; ++i)
        if (a[i] <= b[j])
            ++j, ++ans;

    cout << ans;
}