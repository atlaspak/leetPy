# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first,last = 0,n
        mid = 0
        while(last >= first):
            mid = (last + first) // 2
            if(isBadVersion(mid)):
                last = mid - 1;
            else:
                first = mid + 1
        return first
        
