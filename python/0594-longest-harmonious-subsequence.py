
#time: O(N) space: O(N)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 0

        for key in counter:
            if key + 1 in counter:
                current = counter[key] + counter[key + 1]
                result = max(result, current)
        
        return result