# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left   # both in left subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right  # both in right subtree
            else:
                return root        # split point → LCA
