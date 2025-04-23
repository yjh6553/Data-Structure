# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Find peak
        left = 0
        right = mountainArr.length() - 1

        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        # Binary search on the increasing part
        left1 = 0
        right1 = peak
        while left1 <= right1:
            mid1 = (left1 + right1) // 2
            val = mountainArr.get(mid1)
            if val == target:
                return mid1
            elif val < target:
                left1 = mid1 + 1
            else:
                right1 = mid1 - 1

        # Binary search on the decreasing part
        left2 = peak
        right2 = mountainArr.length() - 1
        while left2 <= right2:
            mid2 = (left2 + right2) // 2
            val = mountainArr.get(mid2)
            if val == target:
                return mid2
            elif val < target:
                right2 = mid2 - 1
            else:
                left2 = mid2 + 1

        return -1 