class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        print(nums)
        longest_count = 1
        current_count = 1

        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                continue

            elif nums[i] == nums[i-1] + 1:
                current_count += 1

            else:
                longest_count = max(longest_count, current_count)
                current_count = 1

        return max(longest_count, current_count)
