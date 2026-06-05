class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        returnable = []
        for i in range(len(nums)):
            returnable.append(nums[i])
        for j in range(len(nums)):
            returnable.append(nums[j])
        return returnable