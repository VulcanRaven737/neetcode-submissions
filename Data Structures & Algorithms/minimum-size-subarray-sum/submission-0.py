import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum1 = 0
        count = math.inf

        for right in range(len(nums)):
            sum1 += nums[right]

            while(sum1 >= target):
                count = min(count, right - left + 1)
                sum1 -= nums[left]
                left += 1

        return 0 if count == math.inf else count