class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2*len(nums))
        for vals in range (len(nums)):
            ans[vals] = nums[vals]
            ans[vals + len(nums)] = nums[vals] 

        return ans 
        