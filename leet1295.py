class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall = 0
        for i in nums:
            if i > 9 and i < 100:
                overall += 1
            elif i > 999 and i < 10000:                
                overall += 1
            elif i > 99999 and 1000000:
                overall += 1
            elif i > 9999999 and 100000000:
                overall += 1
        return overall
