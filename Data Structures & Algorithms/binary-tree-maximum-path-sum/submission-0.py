# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def util(self, node, mxSum): 
        if not node:
            return 0
        
        ltps = self.util(node.left, mxSum)
        rtps = self.util(node.right, mxSum)

        # A path that can be extended to the parent
        single_side_path = max(node.val, node.val + max(ltps, rtps))
        # A path that arches through this node (cannot be extended)
        arched_path = max(single_side_path, node.val + ltps + rtps)

        mxSum[0] = max(mxSum[0], arched_path)
        
        return single_side_path

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        mxSum = [-1001]
        self.util(root, mxSum)

        return mxSum[0]
        