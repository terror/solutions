#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define pll pair<ll, ll>

typedef long long ll;
ll INF = 1000000000;

int main() {
  ll n, m, q, s;
  while (cin >> n >> m >> q >> s) {
    if (n == 0 && m == 0 && q == 0 && s == 0) break;

    vector<pll> adj[10001];
    vector<ll> d;
    d.assign(n + 1, INF);

    for (ll i = 0; i < m; i++) {
      ll u, v, w;
      cin >> u >> v >> w;
      adj[u].pb(mp(v, w));
    }

    // dijk
    queue<ll> x;
    x.push(s);
    d[s] = 0;
    while (!x.empty()) {
      ll curr = x.front();
      x.pop();
      for (auto e : adj[curr]) {
        if (d[curr] + e.s < d[e.f]) {
          d[e.f] = d[curr] + e.s;
          x.push(e.f);
        }
      }
    }

    for (ll i = 0; i < q; i++) {
      ll x;
      cin >> x;
      if (d[x] >= INF / 2)
        cout << "Impossible"
             << "\n";
      else
        cout << d[x] << "\n";
    }
    cout << "\n";
  }
}
