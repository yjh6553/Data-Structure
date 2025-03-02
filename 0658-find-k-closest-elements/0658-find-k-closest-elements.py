class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, 0
        res = []

        def findIndex(arr: List[int], x: int) -> int:
            # Find the index of the closest number to x
            diff = float('inf')
            index = -1
            for i, num in enumerate(arr):
                cur_diff = abs(x - num)  # Use x instead of k
                if cur_diff < diff:
                    diff = cur_diff
                    index = i
            return index

        index = findIndex(arr, x)
        res.append(arr[index])  # Append the actual value, not the index

        left = index - 1
        right = index + 1

        while len(res) < k:  # Fix: should be '<' instead of '<='
            if left < 0:
                res.append(arr[right])
                right += 1
                continue
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
                continue  # Fix: Added continue to avoid extra checks

            right_diff = abs(x - arr[right])  # Use x instead of k
            left_diff = abs(x - arr[left])  # Use x instead of k

            if right_diff < left_diff:
                res.append(arr[right])
                right += 1
            else:
                res.append(arr[left])
                left -= 1

        return sorted(res)  # The result should be sorted