class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret_val = -sys.maxsize - 1
        curr_max = 0
        
        for i in nums:
            curr_max += i
            if(curr_max > ret_val):
                ret_val = curr_max
            if(curr_max < 0):
                curr_max = 0
        return ret_val
