class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter()
        total = 0
        for ch in s:
            cnt[ch] += 1
            if(cnt[ch] % 2):
                total += 2
                del cnt[ch]
        
        if cnt:
            total += 1
        return total
        
