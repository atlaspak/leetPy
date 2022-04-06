class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        up_limit = len(nums) - 1
        down_limit = 0
        
        while down_limit <= up_limit:
            mid = (up_limit + down_limit) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                up_limit = mid -1
            else:
                down_limit = mid + 1
        return -1
