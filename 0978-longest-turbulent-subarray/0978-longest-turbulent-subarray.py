class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        @lru_cache(maxsize=None)
        def dp(i: int, prev: int) -> int:
            # Returns the length of the maximum turbulent subarray starting at index i,
            # given that the difference between arr[i-1] and arr[i] had sign "prev"
            # (0 means no previous comparison).
            if i == n - 1:
                return 1  # Only one element left

            diff = arr[i+1] - arr[i]
            if diff == 0:
                return 1  # Equal elements break turbulence

            curr_sign = 1 if diff > 0 else -1

            # We can extend the subarray if we're starting fresh (prev == 0)
            # or if the current difference alternates with the previous sign.
            if prev == 0 or curr_sign != prev:
                return 1 + dp(i+1, curr_sign)
            else:
                return 1

        best = 1
        # Consider every possible starting index.
        for i in range(n):
            best = max(best, dp(i, 0))
        return best