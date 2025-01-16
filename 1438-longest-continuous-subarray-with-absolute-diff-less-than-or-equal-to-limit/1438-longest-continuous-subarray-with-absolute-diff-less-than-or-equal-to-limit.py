class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # Stores indices of max values
        min_deque = deque()  # Stores indices of min values
        left = 0  # Left pointer of the window
        res = 0   # To store the maximum length

        for right in range(len(nums)):
            # Update max_deque (decreasing order)
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Update min_deque (increasing order)
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Shrink the window if the condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove indices outside the window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Update the result with the current window size
            res = max(res, right - left + 1)

        return res