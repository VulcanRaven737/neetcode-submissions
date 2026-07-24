# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_arr = []

        for j in range(len(lists)):
            curr = lists[j]
            while curr != None:
                sorted_arr.append(curr.val)
                curr = curr.next

        sorted_arr.sort()

        dummy = ListNode(-1, None)
        curr = dummy        

        for j in sorted_arr:
            curr.next = ListNode(j, None)
            curr = curr.next
        
        return dummy.next