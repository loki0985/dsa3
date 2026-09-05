class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute suffix minimums: suff_min[i] = min(nums[i..n-1])
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
        
        # Compute prefix maximums on the fly and check stability
        pref_max = 0
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            instability_score = pref_max - suff_min[i]
            
            if instability_score <= k:
                return i
                
        return -1