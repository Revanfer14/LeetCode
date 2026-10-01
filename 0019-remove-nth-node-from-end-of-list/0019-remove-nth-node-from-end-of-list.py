# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head

        curr = ahead = dummy

        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            curr = curr.next
            ahead = ahead.next

        curr.next = curr.next.next

        return dummy.next
