class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        for i in range(len(nums) - 1): # move left pointer
            left = i
            right = len(nums) - 1
            while right > left:
                if nums[left] > nums[right]:
                    nums[right], nums[left] = nums[left], nums[right]
                right -= 1
        


       

        

