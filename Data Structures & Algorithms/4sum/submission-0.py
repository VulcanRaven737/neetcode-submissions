class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        returnable = []


        for i in range(len(nums)):
            temp_list = []
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                temp_list_2 = []
                start = j+1
                end = len(nums) - 1

                while start < end:
                    temp = nums[i] + nums[j] + nums[start] + nums[end]

                    if temp > target:
                        end -= 1
                    elif temp < target:
                        start += 1
                    else:
                        sums = [nums[i], nums[j], nums[start], nums[end]]
                        if sums not in temp_list_2:
                            temp_list_2.append(sums)
                        start += 1

                for value in temp_list_2:
                    temp_list.append(value)

            for vals in temp_list:
                returnable.append(vals)

        return returnable

