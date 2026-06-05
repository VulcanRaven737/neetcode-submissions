class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        returnable = [1] * length

        pre = 1
        for i in range(len(nums)):
            returnable[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(len(nums)-1, -1, -1):
            returnable[j] *= post
            post *= nums[j]

        return returnable    
