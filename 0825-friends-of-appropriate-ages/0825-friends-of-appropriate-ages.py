class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        amount_in_ages = [0] * 121
        total_amount_until = [0] * 121
        unique_ages = set()
        
        for age in ages:
            amount_in_ages[age] += 1
            unique_ages.add(age)

        for i in range(1, len(amount_in_ages)):
            total_amount_until[i] = total_amount_until[i - 1] + amount_in_ages[i]

        total_requests = 0

        for age in unique_ages: 
            lower_bound = max(age // 2 + 7, 0)
            high_bounb = age

            if lower_bound <= high_bounb:
                requests = amount_in_ages[age] * (total_amount_until[hb] - total_amount_until[lb] - 1)
                total_requests += max(0, requests)
