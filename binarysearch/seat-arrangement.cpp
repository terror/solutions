bool solve(int n, vector<int>& seats) {
  for (int i = 0; i < seats.size(); ++i) {
    if (n == 0) return true;

    // Beginning of the list
    if (i == 0 and seats[i] == 0 and (i == seats.size() - 1 or seats[i + 1] == 0)) {
      seats[i] = 1;
      --n;
    // End of the list
    } else if (i == seats.size() - 1 and seats[i] == 0 and seats[i - 1] == 0) {
      seats[i] = 1;
      --n;
    // Middle of two elements in the list
    } else if (seats[i] == 0 and seats[i - 1] == 0 and seats[i + 1] == 0) {
      seats[i] = 1;
      --n;
    }
  }

  return n == 0;
}
