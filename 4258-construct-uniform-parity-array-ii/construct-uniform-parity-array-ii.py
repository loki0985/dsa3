class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        has_even = any(x % 2 == 0 for x in nums1)
        has_odd = any(x % 2 != 0 for x in nums1)

        # 1. All elements are even -> True
        # 2. All elements are odd -> True
        # 3. Minimum element is odd -> True (can convert all even numbers to odd)
        if not has_odd or not has_even or min_val % 2 != 0:
            return True

        return False