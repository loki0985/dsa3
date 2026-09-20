class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for i, ch in enumerate(s, start=1):
            reversed_alphabet_index = 26 - (ord(ch) - ord('a'))
            total_degree += reversed_alphabet_index * i
        return total_degree