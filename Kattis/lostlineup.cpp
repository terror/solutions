#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> ans(n);
    ans[0] = 1;

    for (int i = 2; i <= n; ++i)
    {
        int x;
        cin >> x;
        ans[x + 1] = i;
    }

    for (auto x : ans)
    {
        cout << x << ' ';
    }
}