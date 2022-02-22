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

int main() {
  int n, q, a, b;
  char x;
  cin >> n >> q;
  uf(n);
  while (q--) {
    cin >> x >> a;
    if (x == 't') {
      cin >> b;
      unionSet(a, b);
    } else
      cout << sizeOfSet(a) << "\n";
  }
  return 0;
}
