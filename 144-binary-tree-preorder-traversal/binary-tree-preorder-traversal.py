# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def preorder(node):
            if not node:
                return
            result.append(node.val)   # Step 1: root
            preorder(node.left)       # Step 2: left
            preorder(node.right)      # Step 3: right
        
        preorder(root)
        return result
