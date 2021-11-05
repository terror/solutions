#include "vectorfunctions.h"
#include <bits/stdc++.h>

using namespace std;

void backwards(vector<int> &vec) {
  int i = 0;
  int j = vec.size() - 1;
  while (i <= j) {
    int t = vec[i];
    vec[i] = vec[j];
    vec[j] = t;
    ++i;
    --j;
  }
}

vector<int> everyOther(const vector<int> &vec) {
  vector<int> ret;
  for (int i = 0; i < vec.size(); ++i)
    if (i % 2 == 0)
      ret.push_back(vec[i]);
  return ret;
}

int smallest(const vector<int> &vec) {
  int ret = *max_element(vec.begin(), vec.end());
  for (int i = 0; i < vec.size(); ++i)
    ret = min(ret, vec[i]);
  return ret;
}

int sum(const vector<int> &vec) {
  int s = 0;
  for (int i = 0; i < vec.size(); ++i)
    s += vec[i];
  return s;
}

int veryOdd(const vector<int> &vec) {
  int c = 0;
  for (int i = 0; i < vec.size(); ++i)
    c += vec[i] & 1 && i & 1;
  return c;
}
