class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        

        def getMax(num: List[int]) -> int:
            prev_rob = 0
            max_rob = 0

            for val in num:
                temp = max(max_rob, prev_rob + val)
                prev_rob = max_rob
                max_rob = temp
            
            return max_rob

        return max(getMax(nums[1:]), getMax(nums[:-1]))