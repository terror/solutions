#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define pll pair<ll, ll>

typedef long long ll;
ll INF = 1000000000;

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  ll n, m, q, s;
  while (cin >> n >> m >> q >> s) {
    if (n == 0 && m == 0 && q == 0 && s == 0)
      break;

    vector<pll> adj[10001];
    vector<ll> d;
    d.assign(n + 1, INF);

    for (ll i = 0; i < m; i++) {
      ll u, v, w;
      cin >> u >> v >> w;
      adj[u].pb(mp(v, w));
    }

    // dijk
    priority_queue<pll, vector<pll>, greater<pll>> x;
    x.push(mp(0, s));
    d[s] = 0;
    while (!x.empty()) {
      ll v = x.top().second;
      ll d_v = x.top().first;
      x.pop();
      if (d_v != d[v])
        continue;
      for (auto e : adj[v]) {
        if (d[v] + e.s < d[e.f]) {
          d[e.f] = d[v] + e.s;
          x.push(mp(d[e.f], e.f));
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
