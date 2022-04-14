#include <bits/stdc++.h>

using namespace std;

vector<int> sieve(int limit) {
  bool prime[limit + 1];
  memset(prime, true, sizeof(prime));

  for (int p = 2; p * p <= limit; ++p) {
    if (prime[p])
      for (int i = p * p; i <= limit; i += p)
        prime[i] = false;
  }

  vector<int> ans;
  for (int p = 2; p <= limit; ++p)
    if (prime[p])
      ans.push_back(p);

  return ans;
}

void solve() {
  int n; cin >> n;

  set<pair<int, int> > ans;
  auto primes = sieve(n);
  for (int i = 0; i < primes.size(); ++i) {
    for (int j = 0; j < primes.size(); ++j) {
      if (primes[i] + primes[j] == n) {
        int a = primes[i], b = primes[j];
        if (a > b) swap(a, b);
        ans.insert(make_pair(a, b));
      }
    }
  }

  cout << n << " has " << ans.size() << " representation(s)\n";
  for (auto pair : ans)
    cout << pair.first << "+" << pair.second << '\n';

  cout << '\n';
}

int main() {
  int T; cin >> T;
  while (T--)
    solve();
}
