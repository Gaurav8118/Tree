# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)      # Step 1: left
            result.append(node.val) # Step 2: root
            inorder(node.right)     # Step 3: right
        
        inorder(root)
        return result
