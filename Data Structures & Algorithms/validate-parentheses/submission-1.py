class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for bracks in s:
            if (bracks == '(' or bracks == '{' or bracks == '['):
                stack.append(bracks)
            else:
                if not stack:
                    return False
                    
                temp = stack.pop()
                print(temp)
                if temp == '(' and bracks == ')' or temp == '{' and bracks == '}' or temp == '[' and bracks == ']':
                    continue
                else:
                    return False

        if len(stack) == 0: return True
        return False
        