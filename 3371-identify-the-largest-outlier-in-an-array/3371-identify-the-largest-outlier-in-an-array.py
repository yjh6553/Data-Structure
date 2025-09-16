class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        '''
        total = sum(nums)
        i = 0
        possible_answers = []

        while i <= len(nums) - 1:
            poss_outlier = int((total - nums[i]) / 2)
            if poss_outlier in nums:
                possible_answers.append(nums[i])
            i += 1
        
        return max(possible_answers)
        '''
        total = sum(nums)
        freq = Counter(nums)
        possible_answers = []

        for num in nums:
            if (total - num) % 2 == 0:  # must be even
                poss_outlier = (total - num) // 2
                # temporarily remove num from freq to avoid self-count
                freq[num] -= 1
                if freq[poss_outlier] > 0:
                    possible_answers.append(num)
                freq[num] += 1
        
        return max(possible_answers)
    