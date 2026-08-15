import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = 0
        stack = []
        for i in range(len(tokens)):
            char = tokens[i]
            if char in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    result = num1 + num2
                elif char == '-':
                    result = num1 - num2
                elif char == '*':
                    result = num1 * num2
                elif char == '/':
                    result = num1/num2
                    if result > 0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                stack.append(result)
            else:
                num = int(char)
                stack.append(num)
            #print(stack)
        return stack[-1]

