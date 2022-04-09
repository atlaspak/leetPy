# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if(q.val >= root.val and p.val <= root.val):
            return root
        elif(q.val <= root.val and p.val >= root.val):
            return root
        elif(root.val > q.val):
            node = self.lowestCommonAncestor(root.left, p, q)
        else:
            node = self.lowestCommonAncestor(root.right, p, q)
        return node
