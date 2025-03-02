class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        res = []

        for i, num in enumerate(nums):
            while dq and dq[-1] < num:
                dq.pop()
            dq.append(num)

            if i >= k and nums[i - k] == dq[0]:
                dq.popleft()
            

            if i >= k - 1:
                res.append(dq[0])
        
        return res