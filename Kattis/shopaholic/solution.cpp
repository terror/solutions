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

    sort(v.rbegin(), v.rend());

    ll ans = 0;
    for (int i = 2; i < n; i += 3)
        ans += v[i];

    cout << ans;
    return 0;
}