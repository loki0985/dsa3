class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> count(51, 0);

        // Count how many size-k subarrays contain each number
        for (int i = 0; i + k <= n; i++) {
            set<int> s;

            for (int j = i; j < i + k; j++) {
                s.insert(nums[j]);
            }

            for (int x : s) {
                count[x]++;
            }
        }

        // Find largest integer appearing in exactly one subarray
        for (int x = 50; x >= 0; x--) {
            if (count[x] == 1) {
                return x;
            }
        }

        return -1;
    }
};