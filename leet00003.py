class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = len(s)
        if (strLen == 0):
            return 0
        total = 0
        substr = {}
        firstInd = 0
        for i in range(strLen):
            if s[i] in substr and substr[s[i]] > firstInd:
                firstInd = substr[s[i]]
            substr[s[i]] = i + 1 
            tempTotal = i - firstInd + 1
            if total < tempTotal:
                total = tempTotal
        return total
                
