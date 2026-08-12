class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops == '+':
                temp1 = stack[-1]
                temp2 = stack[-2]
                stack.append(temp1 + temp2)
            elif ops == 'D':
                temp1 = stack[-1]
                stack.append(2 * temp1)
            elif ops == 'C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(ops))

        return sum(stack)
        