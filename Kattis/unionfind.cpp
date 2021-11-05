#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
vi p, setSize;

void uf(int n) {
  p.assign(n + 1, 0);
  for (int i = 0; i < n; ++i)
    p[i] = i;
  setSize.assign(n + 1, 1);
}

int findSet(int i) { return p[i] == i ? i : p[i] = findSet(p[i]); }

bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

int sizeOfSet(int i) { return setSize[findSet(i)]; }

void unionSet(int i, int j) {
  if (isSameSet(i, j))
    return;
  int a = findSet(i), b = findSet(j);
  if (setSize[a] < setSize[b])
    swap(a, b);
  p[b] = p[a];
  setSize[a] += setSize[b];
}

void fast() { ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); }

int main() {
  fast();
  int n, q, a, b;
  char x;
  cin >> n >> q;
  uf(n);
  while (q--) {
    cin >> x >> a >> b;
    if (x == '=') {
      unionSet(a, b);
    } else
      isSameSet(a, b) ? cout << "yes"
                             << "\n"
                      : cout << "no"
                             << "\n";
  }
  return 0;
}
