class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ')':'(', ']': '[', '}': '{' }
        for bracket in s:
            if bracket in mapping:
                top = stack.pop() if stack else ''
                if(mapping[bracket] != top):
                    return False
            else:                
                stack.append(bracket)
        return not stack
