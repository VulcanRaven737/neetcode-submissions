class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, 0, -1):
            temp = target - nums[i]
            if temp in nums[:i:]:
                return [nums.index(temp),i]