class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        stacked = 0
        total = romans[s[-1]]
        for i in range(len(s)-1):
            num1 = romans[s[i]]
            num2 = romans[s[i+1]]
            if(num1 >= num2):
                total += num1
            else:
                total -= num1
            
        return total
