class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        returnable = []
        check = set()
        sorted_arr = sorted(nums)

        for head in range(len(nums) - 2):
            if head > 0 and sorted_arr[head] == sorted_arr[head - 1]:
                continue
            head_next = head + 1
            tail = len(nums) - 1

            while(head_next < tail):
                total = sorted_arr[head] + sorted_arr[head_next] + sorted_arr[tail]

                if(total > 0):
                    tail -= 1
                elif(total < 0):
                    head_next += 1
                else:
                    temp = (sorted_arr[head], sorted_arr[tail], sorted_arr[head_next])
                    if(temp not in check):
                        check.add(temp)
                        returnable.append(list(temp))
                        head_next += 1
                        tail -= 1
                    else:
                        head_next += 1
                        tail -= 1
        return returnable