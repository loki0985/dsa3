class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();

        // Store {value, original index}
        vector<pair<int, int>> a;
        for (int i = 0; i < n; i++) {
            a.push_back({nums[i], i});
        }

        sort(a.begin(), a.end());

        vector<int> ans = nums;

        int start = 0;

        while (start < n) {
            int end = start;

            // Find one connected component.
            while (end + 1 < n &&
                   (long long)a[end + 1].first - a[end].first <= limit) {
                end++;
            }

            // Collect original indices and values of this component.
            vector<int> indices;
            vector<int> values;

            for (int i = start; i <= end; i++) {
                values.push_back(a[i].first);
                indices.push_back(a[i].second);
            }

            // To get lexicographically smallest result:
            // smallest values go to smallest original indices.
            sort(indices.begin(), indices.end());

            for (int i = 0; i < (int)indices.size(); i++) {
                ans[indices[i]] = values[i];
            }

            start = end + 1;
        }

        return ans;
    }
};