#include <bits/stdc++.h>

using namespace std;
#define MOD 1000000007
typedef long long ll;
ll n;

ll p(ll b, ll p, ll md)
{
    ll ans = 1;
    for (ll i = 0; i < p; ++i)
        ans = ans * b % md;
    return ans;
}

int main()
{
    cin >> n, cout << p(2, n, MOD) << endl;
    return 0;
}