class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        d = 4
        while 10**(d - 1) <= n:
            start = 10**(d - 1)
            end = min(n, 10**d - 1)
            count = end - start + 1
            commas_per_number = (d - 1) // 3
            total_commas += count * commas_per_number
            d += 1
        return total_commas