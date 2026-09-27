class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Pop characters until we find the matching '('
                curr_chars = []
                while stack and stack[-1] != '(':
                    curr_chars.append(stack.pop())
                # Pop the '(' itself
                if stack and stack[-1] == '(':
                    stack.pop()
                # Push the reversed characters back onto the stack
                for c in curr_chars:
                    stack.append(c)
            else:
                stack.append(char)
        
        return "".join(stack)