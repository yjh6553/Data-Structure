class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num
        num_list = []
        for digit in str(num):
            num_list.append(digit)
        
        last = {d : i for i, d in enumerate(num_list)}

        for i in range(len(num_list)):
            for j in range(9, int(num_list[i]), -1):
                j = str(j)
                if j in last and last[j] > i:
                    num_list[i], num_list[last[j]] = num_list[last[j]], num_list[i]
                    return int(''.join(num_list))
        
        return num