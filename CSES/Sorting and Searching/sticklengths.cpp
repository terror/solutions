#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<ll> vl;

ll n;

int main()
{
    cin >> n;
    vl v(n);

    for (auto &x : v)
        cin >> x;

    sort(v.begin(), v.end());

    // median element is the one closest to all other elements
    ll m = v[n / 2];
    ll ans = 0;

    for (auto x : v)
        ans += abs(x - m);
    cout << ans;

    return 0;
}