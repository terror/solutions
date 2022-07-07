vector<int> solve(vector<int>& nums) {
  int n = nums.size();

  if (n < 2)
    return {};

  vector<int> ret;

  for (int i = 0; i < nums.size(); ++i) {
    if (i == 0 and nums[i] > nums[i + 1])
      ret.push_back(i);
    else if (i == nums.size() - 1 and nums[i] > nums[i - 1])
      ret.push_back(i);
    else if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1])
      ret.push_back(i);
  }

  return ret;
}
