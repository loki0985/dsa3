class Solution:

  def resultArray(self, nums: List[int], k: int) -> List[int]:
    result = [0] * k
    dp = [0] * k

    for num in nums:
      val = num % k
      next_dp = [0] * k

      # A new subarray starting at the current element
      next_dp[val] += 1

      # Extend all previous subarrays ending at the last position
      for r in range(k):
        if dp[r] > 0:
          new_r = (r * val) % k
          next_dp[new_r] += dp[r]

      dp = next_dp

      # Accumulate counts into the global result
      for x in range(k):
        result[x] += dp[x]

    return result