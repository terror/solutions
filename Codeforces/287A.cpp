#include <bits/stdc++.h>

// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>

using namespace std;
// using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int, int> pii;
typedef map<int, int> mpii;
typedef set<int> seti;

const int mxN = 2e5, iinf = 1e9 + 10, inf = 1e18 + iinf + 10, mod = 1000000007;
const ld pi = 4.0 * atanl(1.0), prec = .000001;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(c) c.begin(), c.end()
#define rall(c) c.end(), c.begin()
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)

int n, m, t, a[mxN];

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

char adj[100][100];

int dr[] = {1, 0, -1, 0};
int dc[] = {0, 1, 0, -1};

int floodfill(int r, int c, char c1, char c2) {
  // if (r < 0 or r >= 4 or c < 0 or c >= 4) return 0;
  if (adj[r][c] != c1)
    return 0;
  adj[r][c] = c2;
  int ans = 1;

  for (int i = 0; i < 4; ++i) {
    ans += floodfill(r + dr[i], c + dr[i], c1, c2);
  }
  return ans;
}

int main() {
  fast();
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      cin >> adj[i][j];
    }
  }

  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      if (floodfill(i, j, '.', 'x') == 1) {
        cout << "YES";
        return 0;
      }
      floodfill(i, j, 'x', '.');
    }
  }
  cout << "NO";

  return 0;
}
