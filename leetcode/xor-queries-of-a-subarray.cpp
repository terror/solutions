class Solution {
public:
  vector<int> xorQueries(vector<int> &arr, vector<vector<int>> &queries) {
    const int MXN = 2e5;
    vector<int> ret, pre(MXN);
    pre[0] = arr[0];
    for (int i = 1; i < arr.size(); ++i)
      pre[i] = pre[i - 1] ^ arr[i];
    for (int i = 0; i < queries.size(); i++) {
      int l = queries[i][0], r = queries[i][1];
      if (l == 0)
        ret.push_back(pre[r]);
      else
        ret.push_back(pre[r] ^ pre[l - 1]);
    }
    return ret;
  }
};
