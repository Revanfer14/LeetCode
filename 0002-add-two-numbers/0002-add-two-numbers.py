# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        arr1 = []
        arr2 = []

        curr = ListNode(0)
        curr.next = l1

        while curr.next:
            curr = curr.next
            arr1.append(curr.val)

        curr2 = ListNode(0)
        curr2.next = l2

        while curr2.next:
            curr2 = curr2.next
            arr2.append(curr2.val)

        x1 = int("".join(map(str, arr1[::-1])))
        x2 = int("".join(map(str, arr2[::-1])))

        total = x1 + x2

        dummy = ListNode(0)
        cur = dummy

        for c in str(total)[::-1]:
            cur.next = ListNode(int(c))
            cur = cur.next

        return dummy.next