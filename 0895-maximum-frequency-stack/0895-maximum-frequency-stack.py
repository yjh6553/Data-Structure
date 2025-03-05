class FreqStack:

    def __init__(self):
        self.freq_stacks = defaultdict(list)  # key: freq -> value: stack of numbers with that frequency
        self.freq_dict = defaultdict(int)  # key: number -> value: frequency
        self.max_freq = 0  # To keep track of the maximum frequency

    def push(self, val: int) -> None:
        self.freq_dict[val] += 1
        freq = self.freq_dict[val]
        self.freq_stacks[freq].append(val)
        self.max_freq = max(self.max_freq, freq)  # Update max frequency

    def pop(self) -> int:
        most_freq_nums = self.freq_stacks[self.max_freq]
        num = most_freq_nums.pop()
        
        self.freq_dict[num] -= 1
        if not most_freq_nums:  # If no more elements at this frequency, decrease max frequency
            del self.freq_stacks[self.max_freq]
            self.max_freq -= 1

        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()