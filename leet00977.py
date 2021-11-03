class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []
        for num in nums:
            if num < 0:
                stack.append(num * -1)
                continue
            if(stack):
                for stackedVal in reversed(stack):                
                    if(stackedVal <= num):
                        result.append(stackedVal **2)
                        stack.pop()
                    else:
                        break
            result.append(num **2 )
        if(stack):
            for stackedVal in reversed(stack):
                result.append(stackedVal **2)
        
        return result
            
