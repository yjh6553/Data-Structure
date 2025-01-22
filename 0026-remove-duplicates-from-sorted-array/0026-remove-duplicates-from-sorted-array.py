class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        for _ in range(1, len(nums)):
            if nums[left] == nums[right]:
                nums.pop(right)
                right -= 1
            else:
                left = right
            right += 1
