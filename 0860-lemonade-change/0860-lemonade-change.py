class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 1. Use counter to track down all the bills
        # 2. How to calculate the change: used orderedDict to use the biggest one

        
        cashier = defaultdict(int)

        for bill in bills:
            if bill == 5:
                cashier[5] = cashier.get(5, 0) + 1
            if bill == 10:
                if cashier[5] < 1:
                    return False
                cashier[10] = cashier.get(10, 0) + 1
                cashier[5] -= 1
            if bill == 20:
                if cashier[10] >= 1:
                    if cashier[5] == 0:
                        return False
                    else:
                        cashier[10] -= 1
                        cashier[5] -= 1
                elif cashier[5] >= 3:
                    cashier[5] -= 3
                else:
                    return False
        
        return True