class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speeds = []
        stack = []

        for j in range(len(position)):
            speeds.append((position[j], speed[j]))

        speeds.sort()

        for k in range(len(speeds) - 1, -1, -1):
            if not stack or ((target - speeds[k][0])/speeds[k][1]) > stack[-1]:
                stack.append((target - speeds[k][0])/speeds[k][1])
            
        return len(stack)       