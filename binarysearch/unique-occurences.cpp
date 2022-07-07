bool solve(vector<int>& nums) {
  unordered_map<int, int> mp;
  for (int i = 0; i < nums.size(); ++i)
    ++mp[nums[i]];

  set<int> s;
  for (auto u : mp)
    s.insert(u.second);

  return s.size() == mp.size();
}
