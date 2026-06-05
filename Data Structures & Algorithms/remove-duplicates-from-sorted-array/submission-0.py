class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = set(nums)
        checker = sorted(check)
        unique = len(check)
        
        for i in range(unique):
            nums[i] = checker[i]

        return unique
        