#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int max = 0;
        int c = 0;

        for (int i = 0; i < n; ++i)
        {
            char s;
            cin >> s;
            if (s == ')')
            {
                c -= 1;
            }
            else
            {
                c += 1;
            }
            max = min(c, max);
        }

        cout << -max << endl;
    }
    return 0;
}