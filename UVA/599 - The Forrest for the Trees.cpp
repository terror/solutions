#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int, int> ii;
typedef map<int, int> MPII;
typedef set<int> SETI;

const int mxN = 2e5;
const ld pi = 4.0 * atanl(1.0);
const int iinf = 1e9 + 10;
const int inf = 1e18 + iinf + 10;
const int mod = 1000000007;
const ld prec = .000001;

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define all(c) c.begin(), c.end()
#define rall(c) c.end(), c.begin()

const int MXN = 2e5;

int n, m, t, a[mxN];
vi v;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

void dfs(int v, vi adj[], bool vis[]) {
    vis[v] = 1;
    for (auto u : adj[v]) {
        if (!vis[u]) {
            vis[u] = 1;
            dfs(u, adj, vis);
        }
    }
}

int cc(int v, vi ed, vi adj[], bool vis[]) {
    int ans = 0;
    for (int i = 0; i < ed.size(); ++i) vis[i] = 0;
    for (int i = 0; i < ed.size(); ++i) {
        if (!vis[ed[i]]) {
            ++ans;
            dfs(ed[i], adj, vis);
        }
    }
    return ans;
}

// tle :(
int main() {
    int T;
    cin >> T;
    while (T--) {
        string s;
        vi adj[MXN], ed;
        bool vis[MXN];
        while (cin >> s and s.find("*") == string::npos) {
            int u = s[1], v = s[3];
            adj[u].pb(v);
            adj[v].pb(u);
            ed.pb(v);
            ed.pb(u);
        }
        cin >> s;
        int ac = 0;
        for (int i = 0; i < s.size(); i += 2)
            if (find(ed.begin(), ed.end(), s[i]) == ed.end()) ++ac;
        int ans = 0;
        if (ed.size() != 0) ans = cc(ed[0], ed, adj, vis);
        cout << "There are " << ans << " tree(s) and " << ac << " acorn(s)."
             << "\n";
        fill(vis, vis + MXN, 0);
    }
}

