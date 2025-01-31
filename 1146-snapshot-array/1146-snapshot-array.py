class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)]  # Each index stores a list of [snap_id, value]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Manual binary search to find the largest snap_id <= the given snap_id
        history = self.array[index]
        l, r = 0, len(history) - 1
        while l <= r:
            m = (l + r) // 2
            if history[m][0] <= snap_id:
                l = m + 1  # Look for a larger snap_id
            else:
                r = m - 1  # Look for a smaller snap_id
        
        # Return the value corresponding to the closest snap_id <= given snap_id
        return history[r][1]

        
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)