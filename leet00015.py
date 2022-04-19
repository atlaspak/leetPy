class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ret_val = set()
        bs_map = {}
        for i in range(N):
            bs_map[nums[i]] = i
        for i in range(N):
            for j in range(i+1, N):
                search_for = 0 - (nums[i] + nums[j])
                if search_for in bs_map:
                    s_id = bs_map[search_for]
                    if s_id != i and s_id != j:
                        ret_val.add(tuple(sorted((nums[i],nums[j],search_for))))
                

        return list(ret_val)
        
