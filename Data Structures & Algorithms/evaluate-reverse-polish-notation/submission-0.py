import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for i in tokens:
            if(i not in ops):
                stack.append(i)
            else:
                match i:
                    case "+":
                        x = int(stack.pop())
                        y = int(stack.pop())
                        z = x + y
                        stack.append(z)
                    case "-":
                        x = int(stack.pop())
                        y = int(stack.pop())
                        z = y - x
                        stack.append(z)
                    case "*":
                        x = int(stack.pop())
                        y = int(stack.pop())
                        z = y * x
                        stack.append(z)
                    case "/":
                        x = int(stack.pop())
                        y = int(stack.pop())
                        z = y / x
                        if(z < 0):
                            ret = math.ceil(z)
                        else:
                            ret = math.floor(z)
                        stack.append(ret)

        return int(stack[0])