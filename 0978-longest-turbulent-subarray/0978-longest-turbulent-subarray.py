class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Base case: when the condition does not meet.
        res = 0

        def helper(index: int, version: int, cur: int) -> None:
            nonlocal res
            #Base Case
            if index == len(arr) - 1:
                return
            
            if version == 2: # Second Case
                if index % 2 == 0 and arr[index] > arr[index + 1]:
                    cur += 1
                elif index % 2 != 0 and arr[index] < arr[index + 1]:
                    cur += 1
                else:
                    cur = 0
                res = max(res, cur)
                helper(index + 1, version, cur)
            else: # First Case
                if index % 2 == 0 and arr[index] < arr[index + 1]:
                    cur += 1
                elif index % 2 != 0 and arr[index] > arr[index + 1]:
                    cur += 1
                else:
                    cur = 0
                res = max(res, cur)
                helper(index + 1, version, cur)
            

        helper(0, 1, 0) # First Ccase
        helper(0, 2, 0) # Second Case
        return res + 1