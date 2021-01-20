#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;

    int m = 0;
    int msf = 1;

    for (int i = 0; i < s.length(); i++)
    {
        if (i < s.length() && s[i] == s[i + 1])
        {
            msf += 1;
        }
        else
        {
            if (msf > m)
            {
                m = msf;
            }
            msf = 1;
        }
    }

    cout << m << endl;
}