class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1. Sort the people
        # 2. Create left and righ pointer. Left: min and Right: max
        
        people.sort()
        left, right = 0, len(people) - 1
        res = 0
        print(people) #[1, 2, 2, 3] Limit: 3

        while left <= right: 
            if people[right] == limit:
                right -= 1
            elif people[right] + people[left] <= limit:
                left += 1
                right -= 1 
            else:
                right -= 1

            res += 1

        return res