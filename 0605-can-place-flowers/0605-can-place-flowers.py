class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pre = flowerbed[0]
        l = len(flowerbed)
        count = 0
        if n == 0:
            return True

        for i in range(l):
            tmp = flowerbed[i]
            if flowerbed[i] == 0 and pre == 0 and (i == l -1 or not flowerbed[i + 1]):
                count += 1
                tmp = True
                if count >= n:
                    return True
            pre = tmp
        else:
            return False
            