class Solution:
    def calPoints(self, operations: List[str]) -> int:
        check = 0
        socres = []

        for op in operations:
            if op == "C":
                socres.pop()

            elif op == "D":
                num = socres[-1] * 2
                socres.append(num)

            elif op == "+":
                num = socres[-1] + socres[-2]
                socres.append(num)
            
            else:
                socres.append(int(op))

            print(socres)
        return sum(socres)