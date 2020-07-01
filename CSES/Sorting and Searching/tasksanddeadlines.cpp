#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
#define pb push_back
#define mp make_pair

int n, a, b;

int main()
{
    cin >> n;
    VPII v;

    for (int i = 0; i < n; ++i)
        cin >> a >> b, v.pb(mp(a, b));

    sort(v.begin(), v.end());

    ll sum = 0;
    ll ans = 0;
    for (int i = 0; i < n; ++i)
        sum += v[i].first, ans += v[i].second - sum;

    cout << ans;

    return 0;
}