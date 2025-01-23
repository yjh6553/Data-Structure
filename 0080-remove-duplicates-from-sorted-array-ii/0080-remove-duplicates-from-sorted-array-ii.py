class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1  # Start from the second element
        count = 1  # Count occurrences of the current number
        
        while index < len(nums):
            if nums[index] == nums[index - 1]:  
                count += 1
                if count > 2: 
                    nums.pop(index) 
                    continue  
            else:
                count = 1 
            
            index += 1 
        
        return len(nums)
        



        