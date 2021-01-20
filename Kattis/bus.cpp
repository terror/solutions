#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    while (n--)
    {
        double tot = 0;
        int k;
        cin >> k;

        if (k == 1)
        {
            tot = 1;
        }
        else
        {
            for (int i = 0; i < k; i++)
            {
                tot += 0.5;
                tot *= 2;
            }
        }
        cout << int(tot) << endl;
    }
}