class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, v in enumerate(nums):
            hash_map[target - v] = i

        for i, v in enumerate(nums):
            if v in hash_map and hash_map[v] != i:
                return [hash_map[v], i]