class Solution:
    def isValid(self, s: str) -> bool:

        cTOo = { ')'  : '(',
                 '}'  : '{',
                 ']'  : '['}
        

        stack = []

        for c in s:
            if c in cTOo:
                if not stack:
                    return False
                elif stack[-1] != cTOo[c]:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(c)
        
        return len(stack) == 0

        