class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            bracket = s[i]
            if not stack or bracket in ['[', '(', '{']:
                stack.append(bracket)
            elif stack[-1] == '[' and bracket == ']':
                stack.pop()
            elif stack[-1] == '{' and bracket == '}':
                stack.pop()
            elif stack[-1] == '(' and bracket == ')':
                stack.pop()
            else:
                return False
            
        return  len(stack) == 0
            


        