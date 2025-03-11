class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = ["*"] * k
        self.front = -1  # Initially, front is -1 to indicate an empty queue
        self.rear = -1   # Rear also starts at -1
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():  # Queue is full
            return False

        if self.isEmpty():  # First element being inserted
            self.front = 0

        self.rear = (self.rear + 1) % self.cap
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():  # If queue is empty
            return False

        self.queue[self.front] = "*"  # Mark as empty
        if self.front == self.rear:  # If there was only one element
            self.front = self.rear = -1  # Reset queue to empty state
        else:
            self.front = (self.front + 1) % self.cap  # Move front forward
        
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.cap == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()