# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2
        arr1 = []
        arr2 = []

        while curr1:
            arr1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            arr2.append(curr2.val)
            curr2 = curr2.next

        num1 = int("".join(map(str, arr1[::-1]))) 
        num2 = int("".join(map(str, arr2[::-1])))
        sums = num1 + num2
        # print(num1)
        # print(num2)
        # print(sums)
        arr_result = []

        while sums > 0:
            arr_result.append(sums%10)
            sums = sums // 10
            
        print(arr_result)

        curr3 = ListNode()
        prev = curr3
        temp = curr3.next
        
        if len(arr_result) == 0:
            return curr3

        for nums in arr_result:
            temp = ListNode(nums)
            prev.next = temp
            prev = temp
            temp = temp.next

        return curr3.next
            