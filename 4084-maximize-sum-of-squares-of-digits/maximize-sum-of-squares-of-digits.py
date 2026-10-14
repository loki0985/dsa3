class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the total sum is greater than what `num` digits of 9 can hold, it's impossible.
        if sum > 9 * num or sum < 0:
            return ""
        
        res = []
        rem_sum = sum
        rem_len = num
        
        for i in range(num):
            # We want the largest possible digit for the current position.
            # It can be at most 9, but also cannot leave a remaining sum 
            # greater than what the remaining positions can accommodate (each can take at most 9).
            max_digit = min(9, rem_sum)
            min_digit = max(0, rem_sum - 9 * (rem_len - 1))
            
            # To maximize the score and the number itself, we want the largest digit possible.
            # Wait, to maximize the *score* (sum of squares), larger digits are always better, 
            # and among numbers with the same maximum score, the problem asks for the maximum integer, 
            # which means we want larger digits earlier (standard lexicographical order from left to right).
            # Thus, we pick the largest valid digit for this position.
            
            chosen_digit = min(9, rem_sum - min_digit) + min_digit # effectively max_digit as long as valid constraints hold
            # Let's write it more cleanly:
            # The highest digit we can put here while leaving enough sum for the rest:
            digit = min(9, rem_sum)
            while digit >= 0:
                if rem_sum - digit <= 9 * (rem_len - 1) and rem_sum - digit >= 0:
                    break
                digit -= 1
            
            res.append(str(digit))
            rem_sum -= digit
            rem_len -= 1
            
        return "".join(res)