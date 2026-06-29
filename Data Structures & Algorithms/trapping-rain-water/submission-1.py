class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        count = 0

        while left < right:
            if height[left] > height[right]:
                temp = max_right - height[right]
                if temp > 0:
                    count += temp
                if height[right] > max_right:
                    max_right = height[right]
                right -= 1

            elif height[left] <= height[right]:
                temp = max_left - height[left]
                if temp > 0:
                    count += temp
                if height[left] > max_left:
                    max_left = height[left]
                left += 1

        return count
        