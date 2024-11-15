class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = right

        while (left <= right):
            mid = (left + right) // 2
            current_hours = 0
            for i in piles:
                current_hours += ceil(i / mid)

            if (current_hours <= h):
                k = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return k

