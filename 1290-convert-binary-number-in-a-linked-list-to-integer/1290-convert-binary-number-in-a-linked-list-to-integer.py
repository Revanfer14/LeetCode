# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        curr = head

        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next

        result = int("".join(map(str, arr)), 2)

        return result