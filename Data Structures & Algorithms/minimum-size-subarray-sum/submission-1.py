class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_val = len(nums)
        slow, fast = 0, 0
        accumalate = 0
        
        if sum(nums) < target:
            return 0

        while slow <= fast and fast <= len(nums) - 1:
            accumalate += nums[fast]

            if accumalate < target:
                fast += 1
            elif accumalate >= target:
                min_val = min(min_val, fast - slow + 1)
                accumalate -= nums[slow]
                accumalate -= nums[fast]
                slow += 1

        return min_val