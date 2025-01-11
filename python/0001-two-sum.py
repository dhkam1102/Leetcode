class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, v in enumerate(nums):
            hash_map[target - v] = i

        for i, v in enumerate(nums):
            if v in hash_map and hash_map[v] != i:
                return [hash_map[v], i]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                return [hash_map[num], i]
            else:
                hash_map[target - num] = i
        return [-1, -1]
