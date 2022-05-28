class MyQueue:

    def __init__(self):
        self.que = []
        self.reversed = False

    def push(self, x: int) -> None:
        if self.reversed:
            self.que.reverse()
        self.que.append(x)
        self.reversed = False

    def pop(self) -> int:
        if not self.reversed:
            self.que.reverse()
        self.reversed = True
        return self.que.pop()
    
    def peek(self) -> int:
        if self.reversed:
            return self.que[-1]
        return self.que[0]
    
    def empty(self) -> bool:
        return not self.que

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
