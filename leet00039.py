class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def fill(curray,remain,start):
            if(remain == 0):
                result.append(list(curray))
                return
            if(remain < 0):
                return
            
            for i in range(start,len(candidates)):
                curray.append(candidates[i])
                fill(curray, remain - candidates[i],i)
                curray.pop()
                    
        fill([],target,0)
        return result
