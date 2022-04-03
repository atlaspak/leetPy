class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {nums[0]: 0}
        for i in range(1,len(nums)):
            var = target - nums[i]
            if(var in nums_dict):
                return [i, nums_dict[var]]
            nums_dict[nums[i]] = i
        
