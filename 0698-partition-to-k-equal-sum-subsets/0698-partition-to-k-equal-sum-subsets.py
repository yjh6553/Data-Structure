class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False  # Fixed: This should return False
        
        target_sum = sum(nums) // k  # Fixed: Should divide by k, not 4
        nums.sort(reverse=True)  # Fixed: Sort without reassigning
        
        subsets = [0] * k  # Fixed: Track subset sums instead of lists

        def backtrack(index):
            if index == len(nums):
                return all(s == target_sum for s in subsets)
            
            for i in range(k):
                if subsets[i] + nums[index] <= target_sum:
                    subsets[i] += nums[index]  # Place in current subset
                    if backtrack(index + 1):  # Recursively try next number
                        return True
                    subsets[i] -= nums[index]  # Undo choice (Backtrack)
                
                if subsets[i] == 0:
                    break  # Optimization: Avoid redundant placements in empty subsets
            
            return False
        
        return backtrack(0)
