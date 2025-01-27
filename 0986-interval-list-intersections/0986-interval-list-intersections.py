class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0  # Pointers for firstList and secondList

        while i < len(firstList) and j < len(secondList):
            # Find the start and end of the intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If there's an intersection
            if start <= end:
                result.append([start, end])

            # Move the pointer of the interval that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result