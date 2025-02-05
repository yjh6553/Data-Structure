class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        for i in range(max(len(v1), len(v2))):
            check1 = v1[i] if len(v1) > i else 0
            check2 = v2[i] if len(v2) > i else 0

            if check1 > check2:
                return 1
            if check1 < check2:
                return -1
        
        return 0