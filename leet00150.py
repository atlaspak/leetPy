class Solution:
    def evalRPN(self, tokens: List[str]) -> int:        
        operate = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        stack = []
        
        for ch in tokens:
            try:
                val = int(ch)
                stack.append(val)
            except ValueError:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(operate[ch](val1, val2))
        return stack.pop()
            
