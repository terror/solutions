#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define all(c) c.begin(), c.end()
#define rall(c) c.end(), c.begin()
#define INF (int)1e9
#define MOD 1000000007
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef map<int, int> MPII;
typedef set<int> SETI;

const int mxN = 2e5;
int a[mxN];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string a, b;
    cin >> a >> b;

    int cnt = 0;
    for (int i = 0; i < a.length(); ++i)
    {
        if (a[i] != b[i])
        {
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}