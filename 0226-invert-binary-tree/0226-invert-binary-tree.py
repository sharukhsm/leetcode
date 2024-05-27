# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if the current node is not None
        if root:
            # Store the left child of the current node
            left = root.left
            
            # Recursively invert the right subtree and assign it to the left child
            root.left = self.invertTree(root.right)
            
            # Recursively invert the left subtree (stored in 'left') and assign it to the right child
            root.right = self.invertTree(left)
        
        # Return the root of the inverted tree
        return root