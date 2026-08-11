class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int n = nums.size();

        // Find the longest sequential prefix
        int sum = nums[0];

        for (int i = 1; i < n; ++i) {
            if (nums[i] == nums[i - 1] + 1) {
                sum += nums[i];
            } else {
                break;
            }
        }

        // Put all numbers into a set for O(1) lookup
        unordered_set<int> st(nums.begin(), nums.end());

        // Find the smallest missing number >= sum
        while (st.count(sum)) {
            ++sum;
        }

        return sum;
    }
};