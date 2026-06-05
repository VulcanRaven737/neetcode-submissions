class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        returnable = {}
        returnable_list = []
        for i in nums:
            if i not in returnable:
                returnable[i] = 1
            else:
                returnable[i] += 1

        check = dict(sorted(returnable.items(), key = lambda item : item[1], reverse = True))
        final_check = list(check.items())

        for i in range(k):
            returnable_list.append(final_check[i][0])            
                    
        return returnable_list
        