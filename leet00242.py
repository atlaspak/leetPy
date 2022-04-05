class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = {}
        
        for ch in s:
            if ch not in counter:
                counter[ch] = 0
            counter[ch] += 1
        
        for ch in t:
            if ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    del counter[ch]
            else:
                return False
        return not counter
        
