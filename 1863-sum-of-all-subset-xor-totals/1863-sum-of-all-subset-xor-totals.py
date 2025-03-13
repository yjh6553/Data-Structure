class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def backtrack(index: int, cur_xor: int) -> None:
            nonlocal res
            res += cur_xor  # Add the XOR sum of the current subset
            
            for i in range(index, n):
                backtrack(i + 1, cur_xor ^ nums[i])  # Include nums[i] in the XOR subset

        backtrack(0, 0)  # Start with index 0 and XOR value 0
        return res

        