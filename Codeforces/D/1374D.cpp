#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, k;
        cin >> n >> k;

        map<int, int> m;
        for (int i = 0; i < n; ++i)
        {
            int x;
            cin >> x;
            if (x % k)
                m[k - x % k]++;
        }
        if (m.empty())
        {
            cout << 0 << endl;
            continue;
        }

        ll ans = 0;
        for (auto x : m)
        {
            ans = max(ans, x.first + (x.second - 1ll) * k);
        }
        cout << ans + 1 << endl;
    }
    return 0;
}