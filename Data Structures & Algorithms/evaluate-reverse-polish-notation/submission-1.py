from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = deque()

        for token in tokens:
            if token not in ops:
                stack.append(token)
                
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())

                if token == '+': 
                    temp = op2 + op1
                    stack.append(temp)

                elif token == '-':
                    temp = op2 - op1
                    stack.append(temp)

                elif token == '*':
                    temp = op2 * op1
                    stack.append(temp)

                else:
                    temp = op2 / op1
                    stack.append(temp)
                
        return int(stack[-1])