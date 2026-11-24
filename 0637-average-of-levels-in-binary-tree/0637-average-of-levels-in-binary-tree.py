# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        res = []
        queue = deque([root])

        while queue:
            curr = 0
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                
                curr += node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            curr = curr / n
            res.append(curr)

        return res

            