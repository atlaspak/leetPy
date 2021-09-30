class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        j = len(x) - 1
        for num in x:
            if num != x[j]:
                return False
            j -= 1
            
        return True
        
