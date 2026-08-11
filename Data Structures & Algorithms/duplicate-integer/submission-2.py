class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = set(nums)
        if len(t) != len(nums):
            return True
        return False