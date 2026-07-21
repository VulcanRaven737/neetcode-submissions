class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for j in nums:
            if j not in check:
                check.add(j)
            else:
                return j