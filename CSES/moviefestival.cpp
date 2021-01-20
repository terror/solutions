#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pll pair<long, long>
#define VPLL vector<pll>
#define pb push_back
#define mp make_pair
int n, a, b, ans = 0, s = 0;
int main() {
    cin >> n;

    VPLL v;
    for (int i = 0; i < n; ++i) cin >> a >> b, v.pb(mp(b, a));

    sort(v.begin(), v.end());

    for (auto x : v)
        if (x.second >= s) s = x.first, ans++;

    cout << ans;

    return 0;
}
