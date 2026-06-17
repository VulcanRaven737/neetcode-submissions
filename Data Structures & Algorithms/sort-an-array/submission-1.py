import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums

    def quicksort(self, nums:List[int], left:int, right:int):
        if left >= right:
            return

        lt = left
        gt = right
        i = lt

        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]

        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt -= 1
            else:
                i += 1

        self.quicksort(nums, left, lt - 1)
        self.quicksort(nums, gt + 1, right)