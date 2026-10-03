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

        slow = fast = head

        while fast and fast.next is not None:
            print(f"Slow: {slow.val}")
            print(f"Fast: {fast.val}")
            fast = fast.next.next
            slow = slow.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next

