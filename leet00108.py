# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        N = len(nums)
        def locate(start_point, end_point) -> Optional[TreeNode]:
            if start_point > end_point:
                return None
            loc = (start_point + end_point) // 2
            curr = TreeNode(nums[loc])            
            curr.right = locate(loc+1, end_point)
            curr.left = locate(start_point, loc-1)
            return curr
        return locate(0,N-1)
