class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = nums.copy()
        for num in temp:
            if num == val:
                nums.remove(val)

        return len(nums)