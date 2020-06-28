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
        string s1, s2;
        cin >> s1 >> s2;

        cout << s1 << endl;
        cout << s2 << endl;

        for (int i = 0; i < s1.length(); i++)
        {
            if (s1[i] != s2[i])
            {
                cout << "*";
            }
            else
            {
                cout << ".";
            }
        }
        cout << "" << endl;
    }
    return 0;
}