class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0
        cmax = 0
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:  # char == '*'
                cmin -= 1  # Treat '*' as ')'
                cmax += 1  # Treat '*' as '('
                
            if cmax < 0:
                return False
            
            # cmin cannot drop below 0 because '*' can be treated as an empty string ""
            if cmin < 0:
                cmin = 0
                
        return cmin == 0