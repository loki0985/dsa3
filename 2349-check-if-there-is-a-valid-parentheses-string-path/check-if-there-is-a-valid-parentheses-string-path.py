from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
            
        @cache
        def dfs(r, c, balance):
            if balance < 0:
                return False
                
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
                
            if balance < 0:
                return False
                
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Try moving down or right
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, balance)
            if c + 1 < n:
                res = res or dfs(r, c + 1, balance)
                
            return res

        return dfs(0, 0, 0)