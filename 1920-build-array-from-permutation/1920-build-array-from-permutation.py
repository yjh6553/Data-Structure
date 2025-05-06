class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prev = nums[i]
            res.append(nums[prev])
        
        return res