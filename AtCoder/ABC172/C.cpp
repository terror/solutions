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
typedef vector<ll> vll;
typedef pair<int, int> pi;
typedef map<int, int> MPII;
typedef set<int> SETI;

const int mxN = 2e5;
int a[mxN];
int n, m, k, x;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> k;

    vll a(n);
    vll b(m);

    for (auto &x : a)
        cin >> x;
    for (auto &x : b)
        cin >> x;

    // prefix sum
    vll sA(n + 1);
    vll sB(m + 1);
    sA[0] = 0, sB[0] = 0;

    for (int i = 0; i < n; ++i)
        sA[i + 1] = sA[i] + a[i];
    for (int i = 0; i < m; ++i)
        sB[i + 1] = sB[i] + b[i];

    ll ans = 0, j = m;
    for (int i = 0; i < n + 1; ++i)
    {
        if (sA[i] > k)
            break;
        while (sB[j] > k - sA[i])
            j -= 1;
        ans = max(ans, i + j);
    }
    cout << ans;

    return 0;
}