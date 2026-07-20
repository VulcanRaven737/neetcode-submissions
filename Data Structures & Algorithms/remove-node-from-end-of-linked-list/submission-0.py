# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        arr_list = []
        
        while tmp:
            arr_list.append(tmp.val)
            tmp = tmp.next

        print(arr_list)
        length = len(arr_list) - n

        prev = head
        curr = head

        for i in range(length):
            prev = curr
            curr = curr.next

        prev.next = curr.next
        
        if prev == curr:
            head = head.next

        return head
        

        