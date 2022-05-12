# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ret_val = None
        def searchNodes(node):
            if not node:
                return False
            
            right = searchNodes(node.right)
            left = searchNodes(node.left)            
            current = node == p or node == q
            
            if current + left + right >= 2:
                self.ret_val = node
            
            return current or left or right
        searchNodes(root)
        return self.ret_val
                
