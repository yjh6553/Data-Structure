class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def maxSlidingWindow(nums, k):
    if not nums:
        return []
    
    result = []
    dq = deque()  # 

    for i in range(len(nums)):
        # Remove elements outside the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements smaller than the current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current element's index
        dq.append(i)

        # Append the maximum to the result once the first window is formed
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result