class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();

        // dp[i] = maximum number of characters from the suffix
        // of word2 that can be matched as a subsequence
        // in word1[i...n-1].
        vector<int> dp(n + 1, 0);

        int j = m - 1;

        // Match word2 from right to left.
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = dp[i + 1];

            if (j >= 0 && word1[i] == word2[j]) {
                dp[i]++;
                j--;
            }
        }

        vector<int> ans;

        int i = 0;
        j = 0;

        // Greedily choose the smallest possible index.
        while (i < n && j < m) {

            // Exact match.
            if (word1[i] == word2[j]) {
                ans.push_back(i);
                i++;
                j++;
            }
            // Use the one allowed character change.
            else {
                int remaining = m - j - 1;

                // After using i as the mismatched character,
                // enough characters must remain to match
                // the rest of word2 exactly.
                if (dp[i + 1] >= remaining) {
                    ans.push_back(i);
                    i++;
                    j++;

                    // The mismatch has been used.
                    break;
                }

                i++;
            }
        }

        // Match the remaining characters exactly.
        while (i < n && j < m) {
            if (word1[i] == word2[j]) {
                ans.push_back(i);
                j++;
            }
            i++;
        }

        // Could not construct a complete sequence.
        if (j != m) {
            return {};
        }

        return ans;
    }
};