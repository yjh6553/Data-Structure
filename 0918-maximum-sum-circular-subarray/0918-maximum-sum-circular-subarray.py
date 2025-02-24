class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        totalSum = 0

        for num in nums:
            curMax = max(curMax, 0) + num
            maxSum = max(maxSum, curMax)

            curMin = min(curMin, 0) + num
            minSum = min(minSum, curMin)

            totalSum += num
        
        if totalSum == minSum:
            return maxSum
        
        return max(maxSum, totalSum - minSum)