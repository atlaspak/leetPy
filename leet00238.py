class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        total = 1
        once = False
        twice = False
        for i in nums:
            if i == 0:
                if once == True:
                    twice = True
                    break
                once = True                
                continue
            total *= i
            
            
        for i in nums:
            if twice:
                result.append(0)
                continue
            if once:
                if i == 0:
                    result.append(total)
                else:
                    result.append(0)
                continue
            result.append(total // i)
        
        return result
