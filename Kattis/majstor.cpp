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

const ll MXN = 1e9 + 10;

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

ll n, m;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }

ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

char solve(char mv) {
    if (mv == 'P') return 'R';
    if (mv == 'R') return 'S';
    if (mv == 'S') return 'P';
    return -1;
}

int main() {
    int ans1 = 0, ans2 = 0;
    string s1, s2;
    cin >> n >> s1 >> m;
    map<int, map<int, int> > mp;
    while (m--) {
        cin >> s2;
        for (int i = 0; i < n; ++i) {
            ++mp[i][s2[i]];
            if ((s1[i] == 'P' and s2[i] == 'S') ||
                (s1[i] == 'S' and s2[i] == 'R') ||
                (s1[i] == 'R' and s2[i] == 'P'))
                continue;
            if (s1[i] == s2[i]) {
                ++ans1;
                continue;
            }
            ans1 += 2;
        }
    }
    char moves[3] = {'P', 'S', 'R'};
    for (auto x : mp) {
        int mx = 0;
        for (auto u : moves) mx = max((2 * x.s[solve(u)]) + x.s[u], mx);
        ans2 += mx;
    }
    cout << ans1 << "\n" << ans2 << "\n";
}
