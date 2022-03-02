#include "arithmeticfunctions.h"

#include <bits/stdc++.h>

using namespace std;

int cube(int x) {
  return pow(x, 3);
}

int max(int x, int y) {
  if (x > y)
    return x;
  return y;
}

int difference(int x, int y) {
  return x - y;
}
