#pragma GCC optimize("O3")
#pragma GCC target("sse4")

#include <bits/stdc++.h>
using namespace std;

// template {{{
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;

const int MXN = 2e5, IINF = 1e9 + 10, INF = 1e18 + IINF + 10, MOD = 1000000007;
const ld PI = 4.0 * atanl(1.0), PREC = .000001;
const char nl = '\n';

#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define F0R(a) for (int i = 0; i < (a); ++i)
#define FORd(i, a, b) for (int i = (b)-1; i >= a; --i)
#define F0Rd(a) for (int i = (a)-1; ~i; --i)
#define trav(a, x) for (auto& a : x)

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.end(), x.begin()
#define lb lower_bound
#define ub upper_bound
#define sz(x) (int)(x).size()
#define ins insert

template <typename T>
void ckmin(T& a, const T& b) {
    a = min(a, b);
}
template <typename T>
void ckmax(T& a, const T& b) {
    a = max(a, b);
}

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }
// }}}

int main() {
    fast();
    int n, cas = 1;
    while (cin >> n) {
        cout << "Case " << cas++ << ":" << nl;
        int a[MXN], m;
        F0R(n) cin >> a[i];
        sort(a, a + n);
        cin >> m;
        while (m--) {
            ll q;
            cin >> q;
            ll ans = INF, ans1 = 0;
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    if (abs(q - (a[i] + a[j])) < ans) {
                        ans = abs(q - (a[i] + a[j]));
                        ans1 = a[i] + a[j];
                    }
                }
            }
            cout << "Closest sum to " << q << " is " << ans1 << "." << nl;
        }
    }
    return 0;
}

