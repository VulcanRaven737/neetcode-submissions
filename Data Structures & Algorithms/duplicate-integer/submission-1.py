class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = set()
        for i in range (len(nums)):
            if nums[i] in t:
                return True
            else:
                t.add(nums[i])

        return False