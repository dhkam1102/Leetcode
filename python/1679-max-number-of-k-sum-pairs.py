class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        hash_map  = {}
        pairs = 0
        for num in nums:
            if k - num in hash_map and hash_map[k- num] >= 1:
                pairs += 1
                hash_map[k - num] -= 1

            else:
                hash_map[num] = hash_map.get(num, 0) + 1

        return pairs