class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        
        for ch in ransomNote:
            if counter[ch] is None or counter[ch] == 0:
                return False
            else:
                counter[ch] -= 1
        return True
