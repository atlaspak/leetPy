class Solution:
    def climbStairs(self, n: int) -> int:        
        first, second = 1,2
        if n == 1 or n == 0 or n == 2:
            return n
        
        for i in range(3,n+1):
            next_ = first + second
            first, second = second,next_
        return second
