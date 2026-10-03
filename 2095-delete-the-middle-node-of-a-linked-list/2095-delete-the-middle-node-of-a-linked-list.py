# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        ahead = head

        while ahead and ahead.next is not None:
            ahead = ahead.next.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next

