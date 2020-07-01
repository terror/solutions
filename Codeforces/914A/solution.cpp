#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int mx = INT_MIN;

    for (int i = 0; i < n; ++i)
    {
        int x;
        cin >> x;
        bool ok = false;
        for (int i = 0; i * i <= x; ++i)
        {
            if (i * i == x)
            {
                ok = true;
            }
        }
        if (!ok)
            mx = max(mx, x);
    }

    cout << mx << endl;
    return 0;
}