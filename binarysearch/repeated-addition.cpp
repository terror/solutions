int solve(int n) {
  int outer = n;

  while (1) {
    int inner = 0;

    while (outer != 0) {
      inner += outer % 10;
      outer /= 10;
    }

    if (inner < 10)
      return inner;

    outer = inner;
  }
}
