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
ll n;
int main()
{
    ios::sync_with_stdio(0), cin.tie(0);

    cin >> n;
    vll a(n + 1);
    for (ll i = 1; i <= n; ++i)
        for (ll j = i; j <= n; j += i)
            ++a[j];

    ll ans = 0;
    for (ll i = 1; i <= n; ++i)
        ans += (a[i]) * i;

    cout << ans << '\n';
    return 0;
}