class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        current, maxx = 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                else:
                    while nums[left] != 0 and left < right:
                        left += 1
                    left += 1
            current = right - left + 1
            maxx = max(current, maxx)
        return maxx
                    
