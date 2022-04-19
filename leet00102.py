# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret_val = []
        cur_que, next_que = [], []
        
        if root is not None:
            cur_que.append(root)
            ret_val.append([root.val])
            
        while cur_que:
            cur_level = []
            for cur_node in cur_que:
                if cur_node.left:
                    cur_level.append(cur_node.left.val)
                    next_que.append(cur_node.left)
                if cur_node.right:
                    cur_level.append(cur_node.right.val)
                    next_que.append(cur_node.right)
            if cur_level:
                ret_val.append(cur_level)
            cur_que, next_que = next_que, cur_que
            next_que.clear()
        return ret_val
