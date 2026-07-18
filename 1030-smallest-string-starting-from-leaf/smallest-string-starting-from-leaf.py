# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root):
        self.smallest = "~"  # '~' is lexicographically larger than 'z'
        
        def dfs(node, path):
            if not node:
                return
            
            # prepend current char (leaf-to-root order)
            path = chr(ord('a') + node.val) + path
            
            # if leaf, check candidate
            if not node.left and not node.right:
                if path < self.smallest:
                    self.smallest = path
            
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return self.smallest
