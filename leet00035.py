class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        small = 0
        large = len(nums) - 1
        
        while small<=large:
            middle = (small + large) >> 1
            if(nums[middle] == target):
                return middle
            elif(target > nums[middle]):
                small = middle + 1
            else:
                large = middle -1
            
        return small
