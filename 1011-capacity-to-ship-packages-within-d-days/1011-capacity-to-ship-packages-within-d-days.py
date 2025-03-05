class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Check days
        def check_days(cap: int) -> int:
            res = 0
            i = 0

            while i < len(weights):
                cur_total = 0
                while i < len(weights) and cur_total + weights[i] <= cap:
                    cur_total += weights[i]
                    i += 1
                res += 1

            return res

        # Binary Search
        temp = 0
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            total_days = check_days(mid)
            if total_days <= days:
                right = mid
            else:
                left = mid + 1

        return left
