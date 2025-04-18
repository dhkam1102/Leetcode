class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        sample = [0] + flowerbed + [0]

        for i in range(1, len(sample) - 1):
            if sample[i] == 0 and sample[i + 1] == 0 and sample[i -1] == 0:
                n -= 1
                sample[i] = 1
        
        return n <= 0