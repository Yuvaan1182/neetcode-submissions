# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        if node.left == None and node.right == None:
            return 1
        
        lt = self.solve(node.left)
        rt = self.solve(node.right)

        return 1 + max(lt, rt)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)