class Solution:
   def sortColors(self, nums):
    left, cur, right = 0, 0, len(nums)-1
    
    while cur <= right:
        if nums[cur] == 0:
            nums[left], nums[cur] = nums[cur], nums[left]
            cur += 1
            left += 1
            print(cur)
            print(nums)
        elif nums[cur] == 1:
            cur += 1
            print(cur)
            print(nums)
        else:
            nums[cur], nums[right] = nums[right], nums[cur]
            right -= 1
            print(cur)
            print(nums)
            
            