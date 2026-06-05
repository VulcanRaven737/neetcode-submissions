class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if (i != "C" and i != "D" and i != "+"):
                stack.append(int(i))
            elif (i == "+"):
                temp1 = stack[-1]
                temp2 = stack[-2]
                stack.append(temp1 + temp2)
            elif (i == "D"):
                temp1 = stack[-1]
                stack.append(temp1 * 2)
            else:
                stack.pop()

        return sum(stack)
        