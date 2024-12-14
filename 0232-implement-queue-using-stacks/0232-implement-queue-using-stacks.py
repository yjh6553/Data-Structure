class MyQueue:

    def __init__(self):
        self.stack_in = []  # Used for enqueue operation
        self.stack_out = []  # Used for dequeue operation

    def push(self, x: int) -> None:
        # Add an element to the end of the queue
        self.stack_in.append(x)

    def pop(self) -> int:
        # Remove the element from the front of the queue
        self._transfer()
        return self.stack_out.pop()

    def peek(self) -> int:
        # Get the front element
        self._transfer()
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Check if the queue is empty
        return not self.stack_in and not self.stack_out

    def _transfer(self) -> None:
        # Transfer elements from stack_in to stack_out if stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()