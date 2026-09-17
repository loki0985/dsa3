class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = 10**9

        # best[i] = shortest valid subarray with sum=target
        # completely inside arr[0..i]
        best = [INF] * n

        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # A previous subarray must end before 'left'
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                best[right] = length

            # Carry the best previous subarray forward
            if right > 0:
                best[right] = min(best[right], best[right - 1])

        return -1 if ans == INF else ans