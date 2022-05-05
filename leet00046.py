class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)
        def mutate(start):
            if start == N:
                result.append(nums[:])
            for i in range(start,N):
                nums[start], nums[i] = nums[i], nums[start]
                mutate(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        
        mutate(0)
        return result
