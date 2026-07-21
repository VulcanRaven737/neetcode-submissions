# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = head
        start_prev = dummy
        start_val = 1

        while start and start_val != left:
            start_prev = start_prev.next
            start = start.next
            start_val += 1            

        prev, end = None, start

        for _ in range(right - left + 1):
            temp = end.next
            end.next = prev
            prev = end
            end = temp

        start.next = end
        start_prev.next = prev

        return dummy.next




        