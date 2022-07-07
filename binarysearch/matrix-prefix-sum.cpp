vector<vector<int>> solve(vector<vector<int>>& matrix) {
  if (matrix.size() == 0)
    return matrix;

  int r = matrix.size(), c = matrix[0].size();

  for (int i = 1; i < r; ++i)
    for (int j = 0; j < c; ++j)
      matrix[i][j] += matrix[i - 1][j];

  for (int i = 0; i < r; ++i)
    for (int j = 1; j < c; ++j)
      matrix[i][j] += matrix[i][j - 1];

  return matrix;
}
