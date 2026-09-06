class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[j] represents the number of distinct subsequences of s[0...i-1] 
        # that equal t[0...j-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string t can always be formed once by an empty subsequence
        
        for i in range(1, m + 1):
            # Traverse backwards to use the results from the previous row (i-1)
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]