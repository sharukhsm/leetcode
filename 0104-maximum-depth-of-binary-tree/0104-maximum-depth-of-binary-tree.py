# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: # Base case: If the root is None (empty tree), the depth is 0.
            return 0
        # Recursive calls to find the depth of the left and right subtrees.
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # Return the maximum depth among the left and right subtrees, 
        # plus 1 to account for the current level.
        return 1 + max(left_depth, right_depth)
        