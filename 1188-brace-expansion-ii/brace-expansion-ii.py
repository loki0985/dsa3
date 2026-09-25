class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        n = len(expression)
        
        def parse_expr():
            # expr -> term (',' term)*
            res = parse_term()
            while self.i < n and expression[self.i] == ',':
                self.i += 1  # consume ','
                res |= parse_term()
            return res

        def parse_term():
            # term -> factor factor*
            res = {""}
            while self.i < n and expression[self.i] != '}' and expression[self.i] != ',':
                next_set = parse_factor()
                res = {a + b for a in res for b in next_set}
            return res

        def parse_factor():
            # factor -> letter | '{' expr '}'
            if expression[self.i] == '{':
                self.i += 1  # consume '{'
                res = parse_expr()
                self.i += 1  # consume '}'
                return res
            else:
                j = self.i
                while j < n and expression[j].isalpha():
                    j += 1
                word = expression[self.i:j]
                self.i = j
                return {word}

        return sorted(list(parse_expr()))