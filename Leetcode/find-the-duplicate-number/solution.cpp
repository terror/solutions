#include <bits/stdc++.h>
class Solution
{
public:
    int findDuplicate(std::vector<int> &nums)
    {
        int t = nums[0], h = nums[0];
        while (true)
        {
            t = nums[t];
            h = nums[nums[h]];
            if (t == h)
                break;
        }
        t = nums[0];
        while (t != h)
        {
            t = nums[t];
            h = nums[h];
        }
        return h;
    }
};