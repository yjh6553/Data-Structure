class MyStack:
    def __init__(self):
        self.q = deque([])        

    def push(self, x: int) -> None:
        self.q.append(x)
        print(self.q)

    def pop(self) -> int:
        n = len(self.q)
        for _ in range(n - 1):  # Move first (n-1) elements to the back
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        n = len(self.q)
        for _ in range(n):
            num = self.q.popleft()
            self.q.append(num)
        return num

    def empty(self) -> bool:
        print(self.q)
        if len(self.q) == 0:
            return True
        return False

    


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()