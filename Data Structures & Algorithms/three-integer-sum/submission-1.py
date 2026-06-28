class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        returnable = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = len(nums) - 1
            temp = []
            
            while start < end:
                if nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    temp_list = [nums[i], nums[start], nums[end]]
                    if temp_list in temp:
                        start += 1
                    else:
                        temp.append(temp_list)
                        start += 1

            if not temp:
                continue

            for items in temp:
                returnable.append(items)

        return returnable
