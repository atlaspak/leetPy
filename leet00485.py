class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        overall = 0
        for i in nums:
            if i == 1:
                current += 1
            else:
                current = 0
            if current > overall:
                overall = current
        return overall
        
