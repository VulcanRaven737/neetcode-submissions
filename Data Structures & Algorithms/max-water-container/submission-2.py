class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxer = 0
        start = 0
        end = len(height) - 1

        while start < end:
            area = (end - start) * min(height[end], height[start])
            if area > maxer:
                maxer = area

            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return maxer