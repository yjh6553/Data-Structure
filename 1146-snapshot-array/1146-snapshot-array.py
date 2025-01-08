class SnapshotArray:

    def __init__(self, length: int):
        # Using a list of dictionaries to track changes at specific snapshots
        self.array = [{} for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # Store the value along with the current snapshot ID
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        # Increment the snapshot ID and return the previous one
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Get the history of changes for the given index
        changes = self.array[index]
        keys = sorted(changes.keys())
        
        # Binary search to find the largest snapshot ID <= given snap_id
        l, r = 0, len(keys) - 1
        best_snap = -1
        while l <= r:
            m = (l + r) // 2
            if keys[m] <= snap_id:
                best_snap = keys[m]
                l = m + 1
            else:
                r = m - 1
        
        # If we found a valid snapshot, return the corresponding value
        return changes[best_snap] if best_snap != -1 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)