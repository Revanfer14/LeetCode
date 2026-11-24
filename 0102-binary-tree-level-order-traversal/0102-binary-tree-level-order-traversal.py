# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            n = len(queue)

            curr = []

            for _ in range(n):
                node = queue.popleft()
                curr.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(curr)

        return res