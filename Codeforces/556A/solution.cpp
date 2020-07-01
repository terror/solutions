#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;

    string s;
    cin >> s;

    int z = 0;
    int o = 0;
    for (int i = 0; i < s.length(); ++i)
    {
        if (s[i] == '0')
            z += 1;
        else
            o += 1;
    }
    cout << abs(z - o) << endl;
    return 0;
}