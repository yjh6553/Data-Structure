class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        [1 2 5 6 0 0]

        [1]
        1

        """
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        k = 0
        for i in range(len(nums)):
            if i + 1 >= len(nums):
                break
            if nums[i] <= nums[i+1]:
                k += 1
            else:
                break
        print(k)
        new = nums[k + 1:] + nums[0: k+1]
        print(new)
        # Use binary Search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            if new[mid] == target:
                return True
            if new[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False