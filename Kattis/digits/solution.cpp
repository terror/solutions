#include <bits/stdc++.h>

using namespace std;

int recurr(int c, string s)
{
    int size = s.length();
    if (to_string(size) == s)
        return c;
    return recurr(c + 1, to_string(size));
}

int main()
{
    while (true)
    {
        string s;
        cin >> s;
        if (s == "END")
            break;
        else
            cout << recurr(1, s) << endl;
    }
    return 0;
}
