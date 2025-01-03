class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # for i in range(len(flowerbed)):
        #     left = i == 0 or flowerbed[i - 1] == 0
        #     right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

        #     if left and right and flowerbed[i] == 0:
        #         flowerbed[i] = 1
        #         n -= 1
        
        # return True if n <= 0 else False


        # Check left side and right side of current position to check if it is 0.

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
        
        return True if n <= 0 else False
            
