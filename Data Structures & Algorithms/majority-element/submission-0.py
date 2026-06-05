class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_check = {}

        for i in nums:
            if (i not in dict_check):
                dict_check[i] = 1
            else:
                dict_check[i] += 1

        
        sorted_dict_check = sorted(dict_check.items(), key = lambda val: val [1], reverse = True)
        return sorted_dict_check[0][0]


        