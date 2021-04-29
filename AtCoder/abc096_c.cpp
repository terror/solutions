#pragma GCC optimize("O3")
#pragma GCC target("sse4")

#include <bits/stdc++.h>

// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;

using namespace std;

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

const int MXN = 1001, IINF = 1e9 + 10, INF = 1e18 + IINF + 10, MOD = 1000000007;
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

int n, m;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }

ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

char a[MXN][MXN];

int main() {
    fast();
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == '#') {
                bool p = 0;
                // check all neighbouring cells
                if (i + 1 < n) {
                    if (a[i + 1][j] == '#') p = 1;
                }
                if (i - 1 >= 0) {
                    if (a[i - 1][j] == '#') p = 1;
                }
                if (j + 1 < m) {
                    if (a[i][j + 1] == '#') p = 1;
                }
                if (j - 1 >= 0) {
                    if (a[i][j - 1] == '#') p = 1;
                }
                if (!p) {
                    cout << "No";
                    return 0;
                }
            }
        }
    }
    cout << "Yes";
    return 0;
}

