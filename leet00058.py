class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        write_mode = True
        count = 0
        for ch in s:
            if ch == ' ':
                write_mode = True
            elif write_mode:
                write_mode = False
                count = 1
            else:
                count += 1
        return count
