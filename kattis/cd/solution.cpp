#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    while (n > 0 || m > 0)
    {

        unordered_set<int> s;
        for (int i = 0; i < n; ++i)
        {
            int x;
            cin >> x;
            s.insert(x);
        }

        int c = 0;
        for (int i = 0; i < m; ++i)
        {
            int x;
            cin >> x;
            if (s.count(x))
            {
                c += 1;
            }
        }
        cout << c << endl;
        cin >> n >> m;
    }
}