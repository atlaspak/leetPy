class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_size, s_size = len(p), len(s)
        
        p_count = Counter(p)
        s_count = Counter()
        
        ret_val = []
        for i in range(s_size):
            s_count[s[i]] += 1
            
            if i >= p_size:
                if s_count[s[i-p_size]] == 1:
                    del s_count[s[i-p_size]]
                else:
                    s_count[s[i-p_size]] -= 1
                    
            if p_count == s_count:
                ret_val.append(i - p_size +1)
        
        return ret_val
