class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();

        int mn = 0, mx = 0;

        // Find positions of minimum and maximum
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[mn])
                mn = i;

            if (nums[i] > nums[mx])
                mx = i;
        }

        // Make mn the leftmost position
        if (mn > mx)
            swap(mn, mx);

        // 1. Remove both from front
        int front = mx + 1;

        // 2. Remove both from back
        int back = n - mn;

        // 3. Remove min from front and max from back
        int both = (mn + 1) + (n - mx);

        return min({front, back, both});
    }
};