class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0

        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[write_index] = nums[reader]
                write_index += 1
        
        return write_index
