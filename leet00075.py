class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        
        for color in nums:
            if color == 0:
                zero += 1 
            if color == 1:
                one += 1
            if color == 2:
                two += 1
        
        for i in range(len(nums)):
            if(zero):
                nums[i] = 0
                zero -= 1
            elif(one):
                nums[i] = 1
                one -= 1
            elif(two):
                nums[i] = 2
                two -= 1
        
