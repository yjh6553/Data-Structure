class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_stack = list(num1)
        num2_stack = list(num2)
        cur = 0
        carry = 0
        res = ""

        while num1_stack or num2_stack or carry:
            if num1_stack:
                a = int(num1_stack.pop())
            else:
                a = 0
            if num2_stack:
                b = int(num2_stack.pop())
            else:
                b = 0

            cur = a + b + carry
            carry = cur // 10
            cur = cur % 10
            res = str(cur) + res
        
        return res
        

