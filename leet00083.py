# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev_val = -101
        prev_link = head
        while current:
            if current.val == prev_val:
                prev_link.next = current.next
            else:
                prev_val = current.val
                prev_link = current
            current = current.next
        return head
