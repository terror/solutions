#include <bits/stdc++.h>

using namespace std;
int mxN = 2e5;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> v(m);

    for (auto &x : v)
        cin >> x;

    sort(v.begin(), v.end());
    int best = mxN;

    for (int i = 0; i <= m - n; ++i)
    {
        best = min(best, v[i + n - 1] - v[i]);
    }

    cout << best << endl;
    return 0;
}