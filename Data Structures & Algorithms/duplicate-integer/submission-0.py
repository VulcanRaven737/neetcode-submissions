class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        returnable = len(set(nums))
        actual = len(nums)
        if(returnable != actual):
            return True 
        else:
            return False
