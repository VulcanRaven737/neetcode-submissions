from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        returnable = [0] * len(temperatures)
        stack = deque()

        for index, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                prev = stack.pop()
                returnable[prev] = index - prev

            stack.append(index)

        return returnable
                


        
    