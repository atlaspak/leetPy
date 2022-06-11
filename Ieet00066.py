class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        N = len(digits)
        i = N - 1
        while True:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
                if i == -1:
                    digits.insert(0,1)
                    break
                continue
            break
        return digits
