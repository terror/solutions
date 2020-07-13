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
        int ans = 0;
        while (n != 1)
        {
            if (n % 6 == 0)
                n /= 6;
            else
            {
                if ((n * 2) % 6 == 0)
                {
                    n *= 2;
                }
                else
                {
                    ans = -1;
                    break;
                }
            }
            ans += 1;
        }
        cout << ans << endl;
    }
    return 0;
}