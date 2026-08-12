class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checker = {}
        res = count = 0

        for num in nums:
            if num not in checker:
                checker[num] = 0
            checker[num] += 1

            if count < checker[num]:
                count = checker[num]
                res = num

        return res