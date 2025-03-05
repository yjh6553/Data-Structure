class StockSpanner:

    def __init__(self):
        self.mono_stack = []

    def next(self, price: int) -> int:
        stack = self.mono_stack

        # If stack is empty
        if not stack:
            stack.append((price, 1))
            return 1
        
        if stack:
            num = 1
            # Check and pop until the top element is bigger than current price
            while stack and stack[-1][0] <= price :
                num += stack.pop()[1]
            stack.append((price, num))

            if stack[-1][0] > price:
                stack.append((price, 1))

        return stack[-1][1]
            



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)